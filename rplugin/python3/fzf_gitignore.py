# Copyright (c) 2017-2020 Filip Szymański. All rights reserved.
# Use of this source code is governed by an MIT license that can be
# found in the LICENSE file.

import re
import socket
import urllib.error
import urllib.request

import pynvim

__version__ = '1.1'

API_URL = 'https://www.gitignore.io/api/{}'
USER_AGENT = 'fzf-gitignore/{}'.format(__version__)


@pynvim.plugin
class FzfGitignore():
    def __init__(self, nvim):
        self.cache = []
        self.nvim = nvim
        self.newline_re = re.compile(r'\n')

    def error(self, msg):
        self.nvim.command(
            'echohl ErrorMsg | echomsg "[fzf-gitignore] {}" | echohl None'.format(msg))

    def fetch(self, params):
        req = urllib.request.Request(API_URL.format(params))
        req.add_header('User-Agent', USER_AGENT)
        try:
            with urllib.request.urlopen(req, timeout=30) as f:
                data = f.read().decode('utf-8')

                if 'Content-Length' in f.info():
                    if len(data) != int(f.info()['Content-Length']):
                        raise urllib.error.URLError('Download incomplete')

                return data
        except (urllib.error.HTTPError, urllib.error.URLError) as err:
            self.error('{}: {}'.format(err, req.get_full_url()))
            raise
        except socket.error as err:
            self.error('Socket error: {}: {}'.format(err, req.get_full_url()))
            raise
        except socket.timeout as err:
            self.error('Connection timed out: {}: {}'.format(err, req.get_full_url()))
            raise

    @pynvim.function('_fzf_gitignore_get_all_templates', sync=True)
    def get_all_templates(self, args):
        if not self.cache:
            data = self.newline_re.sub(',', self.fetch('list'))
            self.cache = data.split(',')

        return self.cache

    @pynvim.function('_fzf_gitignore_create', sync=True)
    def create(self, args):
        data = self.fetch(','.join(args[0]))
        return data.split('\n')

# vim: ts=4 et sw=4
