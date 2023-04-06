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

# [2]. Tools

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


