# Setup VMware for playing CTF Pwnable challenges in Ubuntu 20.04

>DATE: 06/04/2023 - Ubuntu 18.04 | Ubuntu 20.04 | Ubuntu 22.04 .

## [1]. Install "Oh My ZSH!" and VMware Tools

* It's not really to play the pwn CTF challenge but it optimizes your performance when pwning.

### 1.1. VMware Tools

```bash
# open-vm-tools 
sudo apt-get install open-vm-tools-desktop -y && \ 
reboot
```

**NOTE**: Ubuntu 22.04: error network -> fix `sudo apt-get install open-vm-tools-desktop -y` .

* Check VMware Tools.

```bash
lsb_release -a
```

### 1.2. "Oh My ZSH!"

```bash
sudo apt-get install git zsh curl && sudo chsh -s $(which zsh) && sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && \
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

* Now change content file ~/.zshrc.

```bash
# $ nano ~/.zshrc
	+) ZSH_THEME="half-life" 
	# or "lukerandall"
	# or "frontcube"
	...
	+) plugins=(
		git
	   	zsh-autosuggestions
	   )  
	...
```

**Setting Terminal run zsh default:**

* `Preferences/Unnamed/Command/Run a custom command instead of my shell/Custom command: zsh -> source ~/.zshrc` .

* [how-to-make-zsh-the-default-shell-use-cmd](https://askubuntu.com/questions/131823/how-to-make-zsh-the-default-shell) .


**NOTE**: zsh corrupt history file /home/<user_name>/.zsh_history, fix:

```bash
#!/usr/bin/env zsh
# Fixes a corrupt .zsh_history file

mv ~/.zsh_history ~/.zsh_history_bad
strings -eS ~/.zsh_history_bad > ~/.zsh_history
fc -R ~/.zsh_history
rm ~/.zsh_history_bad

# or $ cd ~ && mv .zsh_history .zsh_history_bad && strings -eS .zsh_history_bad > .zsh_history && fc -R .zsh_history
```
* Create file bash name `zsh_history_fix` and add into `/usr/bin`.

```bash
chmod +x zsh_history_fix && sudo cp zsh_history_fix /usr/bin && cd ../
```

### 1.3. Terminator

```bash
sudo apt-get update && sudo apt-get install terminator && \
sudo apt-get update -y && sudo apt-get dist-upgrade
```


## [2]. Add i386 architecture (to run and compile file ELF x86)

### 2.1. Intel-386
```bash
sudo dpkg --add-architecture i386
```

## [3]. Install Python and Pip

**NOTE:** 

* not recommend use python2 and pip2 `[exploitation kernel tools pip2 error]`.
	
* should use python3 install new versions or use direct python3 in OS Ubuntu.

### 3.1. `Suggest:` [Python3 install new versions](https://github.com/NigmaZ/Blogs/blob/main/Virtual-Machine/Ubuntu/Advanced/README.md#13-python3-new-versions)

### 3.2. Python3 and pip3 (in OS Ubuntu)

```bash
sudo apt-get install python3 python3-dev python3-pip && \
pip3 --version
# pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

* Upgrade pip3

```bash
python3 -m pip install --upgrade pip
```

### 3.3. Python2 and pip2 (not suggest)

```bash
sudo add-apt-repository universe && \
sudo apt update && sudo apt install python2 && \
sudo apt-get install curl && \
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py && \
sudo python2 get-pip.py && \
pip2 --version
# pip 20.0.2 from /usr/local/lib/python2.7/dist-packages/pip (python 2.7)
```

* **NOTE:** [Add PATH](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/)

```
# PYTHON write into ~/.bashrc or ~/.zshrc
export PATH="$HOME/bin:/usr/bin/python3:/bin/python3:/usr/bin/python2:/bin/python2:$PATH"

export PATH="$HOME/bin:/usr/lib/python3/dist-packages/pip:/home/nigma/.local/lib/python3.8/site-packages/pip:/home/nigma/.local/bin:/usr/local/lib/python3.8/dist-packages:/usr/local/lib/python2.7/dist-packages/pip:$PATH"
# cat /etc/environment
# echo $PATH
```

* `source ~/.bashrc` or `source ~/.zshrc`.

## [4]. Install Libraries and support Tools

* Update Ubuntu.

```bash
sudo apt-get update -y && sudo apt-get upgrade
```

### 4.1. Install Tools

```bash
sudo apt-get install -y socat build-essential jq strace ltrace curl wget git make procps vim ssh rubygems gcc dnsutils netcat gcc-multilib net-tools gdb gdb-multiarch libssl-dev libffi-dev libpcre3-dev libdb-dev libxt-dev libxaw7-dev libc6:i386 libncurses5:i386 libstdc++6:i386 patchelf elfutils nasm ascii tree && \
reboot
```

* Brave browser - snap store .

### 4.2. Install Python3 Libraries

```bash
sudo pip3 install pwntools pathlib2 keystone-engine unicorn capstone ropper ipython
```

### 4.3. Install Python2 Libraries

```bash
sudo pip2 install pwntools pathlib2 keystone-engine unicorn capstone ropper ipython
```

## [5]. Install Text Editor

* You can choose 1 of 2

### 5.1. [Sublime Text](https://www.sublimetext.com/docs/linux_repositories.html)

```bash
sudo apt-get install apt-transport-https && \
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg && echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list && sudo apt-get update && sudo apt-get install sublime-text
```

### 5.2. [VS Code](https://code.visualstudio.com/download)

```bash
$ sudo apt update && \
sudo apt install -y software-properties-common apt-transport-https wget  && \
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -  && \
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"  && \
sudo apt update && \
sudo apt install code
```

## [6]. Install tools for Pwnable

### 6.1. Create folder for tools

```bash
cd ~/ && \
mkdir Tools && \
cd Tools
```

(**WORKDIR:** ~/Tools).

### 6.2. pwndbg (Gdb extension)

```
sudo apt-get install libc6-dbg libc6:i386 libc6-dbg:i386
```

```bash
git clone https://github.com/pwndbg/pwndbg && \
cd pwndbg && \
./setup.sh && \
cd ../
```

>plugin-gdb:

* [pwndbg](https://github.com/pwndbg/pwndbg) .

* [gef](https://github.com/hugsy/gef) .

* [gdb-peda](https://github.com/longld/peda) .


**NOTE:** `sudo apt-get install python3-testresources` .

### 6.3. [pwninit](https://github.com/io12/pwninit) (Tools Patching Libc)

* Download the pwninit binary and copy to `/usr/bin/` to excute as a command in terminal.

```bash
mkdir pwninit && \
cd pwninit && \
wget https://github.com/io12/pwninit/releases/download/3.3.0/pwninit && \
chmod +x pwninit && \
sudo cp pwninit /usr/bin/ && \
cd ../
```


### 6.4. [one_gadget](https://github.com/david942j/one_gadget) (Tools for one_gadget searching)

```bash
sudo gem install one_gadget
```

### 6.5. [seccomp-tools](https://github.com/david942j/seccomp-tools) (Analyze seccomp sandbox in CTF pwn challenges)

```bash
sudo apt-get install gcc ruby-dev && \
sudo gem install seccomp-tools && \
sudo apt-get install libseccomp-dev libseccomp2 seccomp
```

### 6.6. [libc-database](https://github.com/niklasb/libc-database)

* Use to find version of libc with offset (more libc than web database).

```bash
git clone https://github.com/niklasb/libc-database && \
cd libc-database && \
sudo apt-get install zstd && \
./get ubuntu && \
cd ../
```

or use libc-database search WEB [libc_serach](https://libc.blukat.me/).

### 6.7. Docker

* You will need to use docker when you want to setup the same environment with the server.

```bash
sudo apt install -y docker.io && \
sudo apt install -y docker-compose
```

### 6.8. IDA Freeware (Tools for reversing)

**NOTE:** `sudo apt-get install libxcb-xinerama0` .

* [Download IDA](https://hex-rays.com/ida-pro/).

```bash
sudo ln -s /opt/idafree-8.1/ida64 /usr/bin  
```

Icon - file `ida64.desktop`.

```bash
[Desktop Entry]
Version=8.1
Name=IDA Freeware 8.1
Exec=/usr/bin/ida64
Icon=/opt/idafree-8.1/appico64.png
Terminal=false
Type=Application
Categories=Application;Development;Utility;
Comment=IDA Freeware 8.1
```

* **Save file this as "ida64.desktop" in folder ~/.local/share/applications**.

* [Youtube Tutorial](https://www.google.com/search?q=how+to+install+ida+freeware+on+ubuntu&biw=1536&bih=758&tbm=vid&sxsrf=ALiCzsbb55gpcDfE0SMX5cbXcN5cGbliDQ%3A1669274367537&ei=_xp_Y9WqINqi-Qbg9bqgBg&oq=h%C6%A1+to+install+ida+for+ubuntu&gs_lcp=Cg1nd3Mtd2l6LXZpZGVvEAMYAjIECCMQJzIGCAAQFhAeMgYIABAWEB4yBggAEBYQHlAAWABg9RBoAHAAeACAAXKIAXKSAQMwLjGYAQDAAQE&sclient=gws-wiz-video#fpstate=ive&vld=cid:caa36be6,vid:3FnyzJ6bTEs).

### 6.9. Ghidra (Tools for reversing)

* If you cannot run the ghidra, checking the ghidra path again, if it alright, try checking `java` (`jdk` and `jre`).

```bash
sudo apt install -y default-jdk default-jre
```

* Version 10.1.5 latest in 01/04/2022, check for new version in [ghidra](https://github.com/NationalSecurityAgency/ghidra/releases).

```bash
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.1.5_build/ghidra_10.1.5_PUBLIC_20220726.zip && \
unzip ghidra_10.1.5_PUBLIC_20220726.zip && \
rm -rf ghidra_10.1.5_PUBLIC_20220726.zip && \
cd ghidra_10.1.5_PUBLIC && \
sudo ln -s ~/Tools/ghidra_10.1.5_PUBLIC/ghidraRun /usr/bin/ghidra && \
cd ../
```

* The command `sudo ln -s ~/Tools/ghidra_10.1.5_PUBLIC/ghidraRun /usr/bin/ghidra` just add the symlink from `ghidraRun` to `/usr/bin/ghidra`, so you can open ghidra with command "ghidra" in terminal.

### 6.10. Radare2

```bash
git clone https://github.com/radare/radare2 && \
cd radare2 && \
sys/install.sh && \
cd ../
```

### 6.11. Fidra

* Use for dynamic reversing.

```
pip3 install frida-tools
```

### 6.12. [Add libc source to gdb](https://github.com/NigmaZ/Blogs/tree/main/Virtual-Machine/Ubuntu/Advanced/FSOP) 

>FSOP attack

* Use when you want to debug deep in libc function like (printf, puts, read, ...), i need to setup this when i learned FSOP attack.

* Download the glibc source code.

```bash
git config --global http.sslverify false && \
git clone https://sourceware.org/git/glibc.git
```

* Setup some scripts for convenient work.

```bash
mkdir add_glibc_source && \
cd add_glibc_source && \
touch add_glibc_source.py && \
nano add_glibc_source.py
```

* Copy and patse this code to `add_glibc_source.py`, edit the path `/home/nigma/` to your path ( this is my scripts, sorry if it so noob :) ).

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

add_all_folder('/home/nigma/Install/glibc/')
```

* We add this script to `.gdbinit`, this will auto add glibc source code when we start gdb.

```bash
echo "source ~/Install/add_glibc_source/add_glibc_source.py" >> ~/.gdbinit
```

* Create another scripts.

```bash
touch libc && \
nano libc
```

* Copy and patse this code to `libc`.

```bash
#!/bin/sh

cd ~/Install/glibc/
git checkout release/$1/master
```

* Add it to `/usr/bin/` to execute as a command.

```bash
chmod +x libc && \
sudo cp libc /usr/bin && \
cd ../
```

* Later if you want to change version of glibc source code, just open the terminal and type `libc + version`, this equal to go to the libc folder and checkout to that version.

### 6.13. Setup qemu 

* [Prepare Kernel](https://github.com/NigmaZ/Blogs/tree/main/Virtual-Machine/Ubuntu/Advanced/Kernel).

* Use for Kernel Exploitation debug.

```
sudo apt install qemu-utils qemu-system-x86
```

* ARM compiler-debug.

```bash
sudo apt install -y qemu-user qemu-user-static gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu binutils-aarch64-linux-gnu-dbg && \
sudo apt install -y gcc-arm-linux-gnueabihf binutils-arm-linux-gnueabihf binutils-arm-linux-gnueabihf-dbg && \
sudo apt-get -y install qemu-kvm qemu
```


# [7]. Finally

* **The article is for general purposes, I recommend that you learn and practice as well as set up tools for the problems you have, do not install all the tools at once and I'm happy to receive your comments.**

>WELL!!!

*These are most of the tools I use to play CTF pwn challenges, there are still a lot of other great tools that I haven't used yet. I want to share so that newbies can start on the path of pwnable. After the installation is complete, you should take a snapshot or compress and store it, in case an error occurs. Older or newer versions of Ubuntu will likely have some errors, but basically I think there won't be too much change in the way of installation. Last word, hope you will find passion or pleasure playing pwnable, goodluck.*

------------------------------------------------

### [+] NOTE FIX:

+ [echo 20 | sudo tee /proc/sys/kernel/watchdog_thresh](https://www.suse.com/support/kb/doc/?id=000018705) .

+ fix error debug when pwn heap. [Fix](https://robbert1978.github.io/posts/Add-dbg_sym-to-libc/)
