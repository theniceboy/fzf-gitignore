# fzf :heart: gitignore.io

[fzf](https://github.com/junegunn/fzf) interface for creating `.gitignore` files using the [gitignore.io](https://www.gitignore.io/) API.
This plugin was inspired by [helm-gitignore](https://github.com/jupl/helm-gitignore).

![](https://user-images.githubusercontent.com/25827968/42945393-96c662da-8b68-11e8-8279-5bcd2e956ca9.png)

## Requirements

* [Nvim](https://neovim.io/)
* [pynvim](https://github.com/neovim/pynvim)
* fzf

## Installation

1. Install Nvim python client.

    ```sh
    pip3 install --upgrade pynvim
    ```

2. Use your favorite Nvim plugin manager to install `fzf-gitignore`.

    **Using [vim-plug](https://github.com/junegunn/vim-plug)**

    ```vim
    Plug 'junegunn/fzf', {'do': {-> fzf#install()}}
    Plug 'fszymanski/fzf-gitignore', {'do': ':UpdateRemotePlugins'}
    ```

## Documentation

For more information, see `:help fzf_gitignore.txt`.

## License

MIT
