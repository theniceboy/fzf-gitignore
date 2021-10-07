scriptencoding utf-8

" Copyright (c) 2017-2020 Filip Szymański. All rights reserved.
" Use of this source code is governed by an MIT license that can be
" found in the LICENSE file.

if exists('g:loaded_fzf_gitignore')
  finish
endif
let g:loaded_fzf_gitignore = 1

if !exists('g:fzf_gitignore_map')
  let g:fzf_gitignore_map = '<Leader>gi'
endif

command! FzfGitignore call fzf_gitignore#run()

if !exists('g:fzf_gitignore_no_maps')
  if !hasmapto('<Plug>(fzf-gitignore)') && empty(maparg(g:fzf_gitignore_map, 'n'))
    execute 'nmap ' . g:fzf_gitignore_map . ' <Plug>(fzf-gitignore)'
  endif
endif

nnoremap <silent> <Plug>(fzf-gitignore) :FzfGitignore<CR>

" vim: ts=2 et sw=2
