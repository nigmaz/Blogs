# Setup Advanced for learn and research Exploit attack
* Heap 
* FSOP
* Sandbox
* Kernel 
* ...

## [1]. ~/.bashrc OR ~/.zshrc, rename user, rename hostname,...

>NOTE: 

   * Add it to `~/.bashrc` or `~/.zshrc` depending on which you use.

   * Rename User: https://youtu.be/k2ZeUkHZSn0
    
   * Rename Hostname: https://www.cyberciti.biz/faq/ubuntu-change-hostname-command/
   
  `hostnamectl set-hostname newhostname`

### 1.1 Alias

```
# ASLR
alias aslr_check='cat /proc/sys/kernel/randomize_va_space'

alias aslr_off="echo 0 | sudo tee /proc/sys/kernel/randomize_va_space"

alias aslr_on="echo 2 | sudo tee /proc/sys/kernel/randomize_va_space"
```

### 1.2. Nasm

```
# nasm -f elf helloworld.asm && ld -m elf_i386 helloworld.o -o helloworld && ./helloworld
# nasm32 <file.asm>
nasm32(){
    filename=${1%.*}
    nasm -f elf $filename.asm; ld -m elf_i386 $filename.o -o $filename #; ./$filename
}
```

```
# nasm -f elf64 hello.asm && ld hello.o -o hello && ./hello
# nasm64 <file.asm>
nasm64(){
    filename=${1%.*}
    nasm -f elf64 $filename.asm; ld $filename.o -o $filename #; ./$filename
}
```

### 1.3. Python3 [new versions]

* [Upgrade Python](https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-10-on-ubuntu-18-04-and-20-04-lts/)

* [Switch PythonVersions](https://www.rosehosting.com/blog/how-to-install-and-switch-python-versions-on-ubuntu-20-04/)

* [Install PythonLatestVersion](https://serverspace.io/support/help/install-python-latest-version-on-ubuntu-20-04/) **[*]**

```bash
curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py && python get-pip.py

# write to ~/.zshrc: export PATH="$HOME/bin:/usr/bin/python:/usr/local/lib/python3.12/dist-packages/pip:$PATH"

sudo pip install pwntools pathlib2 keystone-engine unicorn capstone ropper ipython
```

**Note:** `source ~/.bashrc` or `source ~/.zshrc`.

### 1.4. ~/.gdbinit

```bash
set disassembly-flavor intel
set follow-fork-mode child

# pwndbg-----------------------------------------
source /home/nigma/Tools/pwndbg/gdbinit.py
# -----------------------------------------------


# peda-------------------------------------------
# source /home/nigma/Tools/peda/peda.py
# -----------------------------------------------

# gef--------------------------------------------
# source /home/nigma/Tools/.gdbinit-gef.py

# $ pwd -> in ~/Tools
# $ git clone https://github.com/hugsy/gef.git
# $ echo source `pwd`/gef/gef.py >> ~/.gdbinit
# -----------------------------------------------


# Pwngdb-for-heap--------------------------------
# source ~/Tools/Pwngdb/pwngdb.py
# source ~/Tools/Pwngdb/angelheap/gdbinit.py

# define hook-run
# python
# import angelheap
# angelheap.init_angelheap()
# end
# end
# I use it into gdb-peda and gdb
# ----------------------------------------------
```

### 1.5. Vim

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

### Zsh other

```bash
$ sudo apt-get install git zsh curl 

$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

$ git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

$ sudo chsh -s $(which zsh)

Custome 
$ nano ~/.zshrc
	+) ZSH_THEME="half-life"
	+) plugins=(git
	   zsh-autosuggestions)  

$ source ~/.zshrc


theme powerlevel10k
$ git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

$ Set ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc.

fix icon ubuntu windows terminal 
=> https://github.com/romkatv/powerlevel10k/blob/master/README.md#meslo-nerd-font-patched-for-powerlevel10k

Windows Terminal by Microsoft (the new thing): 
Open Settings (Ctrl+,), click either on the selected profile under 
`Profiles` or on `Defaults`, 
click `Appearance` and set 
`Font face` to `MesloLGS NF`.

$ fix icon vscode 
https://dev.to/avantar/how-to-fix-zsh-icons-in-visual-studio-code-terminal-38bb

vm tools
$ sudo reboot
$ lsb_release -a


```

## [2]. Tools

> Setup tools for reversing as such as IDA, WSL, etc...

* Google

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo apt install ./google-chrome-stable_current_amd64.deb
```


* [Oh My Zsh](https://www.youtube.com/watch?v=Mhdl-qppnlY&list=PL2YJKKcudhJ0ar-IYMehPGRwbcUz8NZJj&index=17&t=1112s) .

* [Wine](https://www.youtube.com/watch?v=Wx8NbZEAPNM&list=PL2YJKKcudhJ0ar-IYMehPGRwbcUz8NZJj&index=18&t=9s) .

* [Burp Suite](https://www.youtube.com/watch?v=-ozGijESmTY&list=PL2YJKKcudhJ0ar-IYMehPGRwbcUz8NZJj&index=3&t=5s) .

* ipyida: https://github.com/eset/ipyida

* WSL: https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/


