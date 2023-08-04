# Setup Advanced for learn and research Exploit attack
- FSOP
- [Fuzzing](https://y3a.github.io/2022/12/14/fuzzing1/)
- Kernel 
- Seccomp

## [1]. ~/.bashrc OR ~/.zshrc, rename user, rename hostname,...
### 1.0. NOTE
- File cấu hình sourcepackge nằm ở /etc/apt/source.list .
- `sudo -s` - root user, `sudo -i` - root .

- [Add and Delete User](https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-ubuntu-18-04) 
```
# Add
sudo adduser <newuser>

groups <newuser>

sudo usermod -aG sudo <newuser>

# Logout user need delete
# Delete
sudo deluser --remove-home <user>
```
    
- [Rename Hostname](https://www.cyberciti.biz/faq/ubuntu-change-hostname-command/)
```
  The procedure to change the computer name on Ubuntu Linux:

  1. Type the following command to edit /etc/hostname using nano or vi text editor:
  sudo nano /etc/hostname
  Delete the old name and setup new name.
  2. Next Edit the /etc/hosts file:
  sudo nano /etc/hosts
  Replace any occurrence of the existing computer name with your new one.
  3. Reboot the system to changes take effect:
  sudo reboot

  OR> $ hostnamectl <current-hostname> <new-hostname>
```

- Change username

```bash
# login usename != has root permisions
sudo usermod -l newUsername oldUsername
sudo groupmod -n newUsername oldUsername
# sudo mv /home/old_username /home/new_username
sudo chown -R new_username:new_username /home/new_username
sudo usermod -d /home/newHomeDir -m newUsername
```

- Change password

```
sudo passwd <user_change_passwd>
```

- Debug process ID with plugin

```
This is due to kernel hardening in Linux; you can disable this behavior by sudo -s && echo 0 > /proc/sys/kernel/yama/ptrace_scope or by modifying it in /etc/sysctl.d/10-ptrace.conf
```

  
- The "`nproc`" command is used to check how many processing units are available or installed in your system. In Linux-like systems, we can have multiple processing units in our system and check them. We use the "`nproc`" command.

- Check port open> `netstat -tulpn | grep ':<port>'`


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

- [Install PythonLatestVersion](https://serverspace.io/support/help/install-python-latest-version-on-ubuntu-20-04/) [*]

```bash
curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py && python get-pip.py

# write to ~/.zshrc: export PATH="$HOME/bin:/usr/bin/python:/usr/local/lib/python3.12/dist-packages/pip:$PATH"

sudo pip install pwntools pathlib2 keystone-engine unicorn capstone ropper ipython
```

### 1.4. ~/.gdbinit

```bash
set disassembly-flavor intel
set follow-fork-mode child
# set max-visualize-chunk-size 0x500

# pwndbg-----------------------------------------
source /home/nigmaz/Public/pwndbg/gdbinit.py
# -----------------------------------------------


# peda-------------------------------------------
# source /home/nigmaz/Public/peda/peda.py
# -----------------------------------------------

# gef--------------------------------------------
# source /home/nigmaz/Public/.gdbinit-gef.py

# $ pwd -> in ~/Public
# $ git clone https://github.com/hugsy/gef.git
# $ echo source `pwd`/gef/gef.py >> ~/.gdbinit
# -----------------------------------------------


# Pwngdb-for-heap--------------------------------
# source ~/Public/Pwngdb/pwngdb.py
# source ~/Public/Pwngdb/angelheap/gdbinit.py

# define hook-run
# python
# import angelheap
# angelheap.init_angelheap()
# end
# end
# I use it into gdb-peda and gdb
# ----------------------------------------------
```

### 1.6. Vim

- Setup vim.
  
  * [Setup1](https://codelearn.io/sharing/cai-dat-vim-editor-than-thanh-phan-1)
  
  * [Setup2](https://codelearn.io/sharing/cai-dat-vim-editor-than-thanh-phan-2)

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

### 1.7. Zsh other

* Theme powerlevel10k.

* [Package Font and Icon](https://github.com/NigmaZ/Blogs/tree/main/Virtual-Machine/Note/MesloLGS%20NF).

```bash
$ git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

$ Set ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc.

* fix icon ubuntu windows terminal 
=> https://github.com/romkatv/powerlevel10k/blob/master/README.md#meslo-nerd-font-patched-for-powerlevel10k

* Windows Terminal by Microsoft (the new thing): 
Open Settings (Ctrl+,), click either on the selected profile under 
`Profiles` or on `Defaults`, 
click `Appearance` and set 
`Font face` to `MesloLGS NF`.

* fix icon vscode 
https://dev.to/avantar/how-to-fix-zsh-icons-in-visual-studio-code-terminal-38bb
```


## [2]. Tools-Hacking (should use in KALI)

* Google

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo apt install ./google-chrome-stable_current_amd64.deb
```

* [Wine](https://www.youtube.com/watch?v=Wx8NbZEAPNM&list=PL2YJKKcudhJ0ar-IYMehPGRwbcUz8NZJj&index=18&t=9s) .

* [Burp Suite](https://www.youtube.com/watch?v=-ozGijESmTY&list=PL2YJKKcudhJ0ar-IYMehPGRwbcUz8NZJj&index=3&t=5s) .

* ipyida: https://github.com/eset/ipyida

* WSL: https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/


