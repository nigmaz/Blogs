# NASM
>sudo apt-get install nasm

- Setup vim.
  
  [+] [Setup1](https://codelearn.io/sharing/cai-dat-vim-editor-than-thanh-phan-1)
  
  [+] [Setup2](https://codelearn.io/sharing/cai-dat-vim-editor-than-thanh-phan-2)
  
```bash
1) touch ~/.vimrc

2) mkdir -p ~/.vim/pack/vendor/start

3) git clone --depth 1 \
  https://github.com/preservim/nerdtree.git \
  ~/.vim/pack/vendor/start/nerdtree


4) git clone --depth 1 \
  https://github.com/vim-airline/vim-airline \
  ~/.vim/pack/vendor/start/vim-airline

5) git clone --depth 1 \
  https://github.com/vim-airline/vim-airline-themes \
  ~/.vim/pack/vendor/start/vim_airline_themes

6) nano ~/.vimrc 
syntax enable              
syntax on

set number
set shiftwidth=4
set tabstop=4
set autoindent
set expandtab
set showmatch
set clipboard=unnamedplus
set ttimeoutlen=50
set cursorline
set wildmenu
filetype plugin indent on

--------------------------- or
$ git clone --depth 1 \
  https://github.com/sickill/vim-monokai \
  ~/.vim/pack/vendor/start/vim_monokai

let g:airline_theme='light'
colorscheme monokai

--------------------------------------- or
$ git clone --depth 1 \
  https://github.com/dracula/vim.git \
  ~/.vim/pack/vendor/start/dracula

packadd! dracula
colorscheme dracula

--------------------------------------- or
$ git clone --depth 1 \
  https://github.com/arcticicestudio/nord-vim \
  ~/.vim/pack/vendor/start/nord-vim

colorscheme nord
```

- File ~/.bashrc or ~/.zshrc

[+] https://github.com/l1j9m4-0n1/Blogs/tree/main/Bashrc

- Learn Nasm

[+] https://asmtutor.com/

[+] https://www.tutorialspoint.com/assembly_programming/index.htm
