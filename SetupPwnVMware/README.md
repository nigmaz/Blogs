# Setup a simple VMware for playing CTF pwn challenges in Ubuntu 20.04

>DATE: 01/04/2022

### 1) Install "Oh My ZSH!" and VMware Tools (to copy and patse from host)

It's not really to play the pwn CTF challenge but it optimizes your performance when pwning.

* VMware Tools

```bash
$ sudo apt install open-vm-tools open-vm-tools-desktop
$ sudo reboot
```
Check VMware Tools

```bash
$ lsb_release -a
```

* "Oh My ZSH!"

```bash
$ sudo apt-get install git zsh curl
$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
$ git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
$ sudo chsh -s $(which zsh)
```
Now change content file ~/.zshrc

```bash
$ nano ~/.zshrc
```

	+) ZSH_THEME="half-life"
	+) plugins=(git
	   zsh-autosuggestions)  

```bash
$ source ~/.zshrc
```

NOTE:$ zsh: corrupt history file /home/<user_name>/.zsh_history

zsh often get this error when using

fix:
```bash
$ cd ~ && mv .zsh_history .zsh_history_bad && strings -eS .zsh_history_bad > .zsh_history && fc -R .zsh_history
```

* Update ubuntu

```bash
$ sudo apt-get update
```

### 2) Add i386 architecture (to run file ELF x86 (32-bit))

```bash
$ sudo dpkg --add-architecture i386
```

### 3) Install Python and Pip

I use both Python2 and Python3 for play Pwn CTFs

From Ubuntu 20.04, py3 is available in base system and py2 is available to install from the Universe repository.

* Python3 and pip3

```bash
$ sudo apt-get install python3 python3-pip python3-dev
$ pip3 --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

Upgrade pip3

```bash
$ python3 -m pip install --upgrade pip
```

* Python2 and pip2

```bash
$ sudo add-apt-repository universe
$ sudo apt update 
$ sudo apt install python2
$ sudo apt-get install curl 
$ curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
$ sudo python2 get-pip.py
$ pip2 --version
pip 20.0.2 from /usr/local/lib/python2.7/dist-packages/pip (python 2.7)
```
NOTE: Add PATH

### 4) Install needed libraries and support tools

* Update Ubuntu

```bash
$ sudo apt-get update -y
$ sudo apt-get upgrade
```

* Install libraries and tools

```bash
sudo apt-get install -y socat build-essential jq strace ltrace curl wget git make procps vim ssh rubygems gcc dnsutils netcat gcc-multilib net-tools gdb gdb-multiarch libssl-dev libffi-dev libpcre3-dev libdb-dev libxt-dev libxaw7-dev libc6:i386 libncurses5:i386 libstdc++6:i386 patchelf elfutils nasm  
```

* Install python3 libraries

```bash
sudo pip3 install pwntools pathlib2 keystone-engine unicorn capstone ropper
```

* Install python2 libraries

```bash
sudo pip2 install pwntools pathlib2 keystone-engine unicorn capstone ropper
```

### 5) Install Text Editor

You can choose 1 of 2

* Sublime Text 



* VS Code

```bash
sudo apt update && \
sudo apt install -y software-properties-common apt-transport-https wget  && \
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -  && \
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"  && \
sudo apt install code
```

### 5) Install tools for pwn

#### +) Create folder for tools

```bash
cd ~/ && \
mkdir Install && \
cd Install
```

#### +) pwndbg (Gdb extension)

```bash
git clone https://github.com/pwndbg/pwndbg.git && \
cd pwndbg && \
./setup.sh && \
cd ../
```

#### +) ROPgadget (Tools for gadget searching)

* It usually install with pwntools, you can pass if you already can use ROPgadget

```bash
git clone https://github.com/JonathanSalwan/ROPgadget.git && \
cd ROPgadget && \
sudo python setup.py install && \
cd ../
```

#### +) one_gadget (Tools for one_gadget searching)

```bash
sudo gem install one_gadget
```

#### +) seccomp-tools (Tools for seccomp)

```bash
sudo apt install -y gcc ruby-dev && \
sudo gem install seccomp-tools
```

#### +) pwninit (Tools for patching libc)

* Download the pwninit binary and copy to `/usr/bin/` to excute as a command in terminal

```bash
mkdir pwninit && \
cd pwninit && \
wget https://github.com/io12/pwninit/releases/download/3.2.0/pwninit && \
chmod +x pwninit && \
sudo cp pwninit /usr/bin/ && \
cd ../
```

#### +) ghidra (Tools for reversing)

* Version 10.1.12 latest in 8/3/2022, check for new version in [ghidra](https://github.com/NationalSecurityAgency/ghidra/releases)

```bash
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.1.2_build/ghidra_10.1.2_PUBLIC_20220125.zip && \
unzip ghidra_10.1.2_PUBLIC_20220125.zip && \
rm -rf ghidra_10.1.2_PUBLIC_20220125.zip && \
cd ghidra_10.1.2_PUBLIC && \
sudo ln -s ~/Install/ghidra_10.1.2_PUBLIC/ghidraRun /usr/bin/ghidra && \
cd ../
```

* The command `sudo ln -s ~/Install/ghidra_10.1.2_PUBLIC/ghidraRun /usr/bin/ghidra` just add the symlink from `ghidraRun` to `/usr/bin/ghidra`, so you can open ghidra with command "ghidra" in terminal

* If you cannot run the ghidra, checking the ghidra path again, if it alright, try checking `java` (`jdk` and `jre`)

```bash
sudo apt install -y default-jdk default-jre
```

#### +) radare2

```bash
git clone https://github.com/radare/radare2 && \
cd radare2 && \
sys/install.sh && \
cd ../
```

#### +) libc-database

```bash
git clone https://github.com/niklasb/libc-database
```

#### +) docker

* You will need to use docker when you want to setup the same environment with the server

```bash
sudo apt install -y docker.io
```

### 6) Add libc source code to gdb

* Use when you want to debug deep in libc function like (printf, puts, read, ...), i need to setup this when i learned FSOP attack

* Download the glibc source code

```bash
git config --global http.sslverify false && \
git clone https://sourceware.org/git/glibc.git
```

* Setup some scripts for convenient work

```bash
mkdir add_glibc_source && \
cd add_glibc_source && \
touch add_glibc_source.py && \
nano add_glibc_source.py
```

* Copy and patse this code to `add_glibc_source.py`, edit the path `/home/cobra/` to your path ( this is my scripts, sorry if it so noob :)) )

```python
import gdb
import os

def add_all_folder(path):
	gdb.execute('dir ' + path)
	dir = os.listdir(path)
	for i in dir:
		subfolder = path + i + '/'
		if os.path.isdir(subfolder):
			add_all_folder(subfolder)

add_all_folder('/home/cobra/Install/glibc/')
```

* We add this script to `.gdbinit`, this will auto add glibc source code when we start gdb

```bash
echo "source ~/Install/add_glibc_source/add_glibc_source.py" >> ~/.gdbinit
```

* Create another scripts

```bash
touch libc && \
nano libc
```

* Copy and patse this code to `libc`

```bash
#!/bin/sh

cd ~/Install/glibc/
git checkout release/$1/master
```

* Add it to `/usr/bin/` to execute as a command

```bash
chmod +x libc && \
sudo cp libc /usr/bin && \
cd ../
```

* Later if you want to change version of glibc source code, just open the terminal and type `libc + version`, this equal to go to the libc folder and checkout to that version

### 7) Setup qemu

* Use for kernel exploitation or arm compiler-debug

```bash
sudo apt install -y qemu-user qemu-user-static gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu binutils-aarch64-linux-gnu-dbg && \
sudo apt install -y gcc-arm-linux-gnueabihf binutils-arm-linux-gnueabihf binutils-arm-linux-gnueabihf-dbg && \
sudo apt-get -y install qemu-kvm qemu
```
