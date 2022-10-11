# Setup a simple VMware for playing CTF pwn challenges in Ubuntu 20.04

>DATE: 31/07/2022 - Ubuntu 18.04, 20.04, 22.04

### 1) Install "Oh My ZSH!" and VMware Tools (to copy and patse from host)

It's not really to play the pwn CTF challenge but it optimizes your performance when pwning.

* VMware Tools

```bash
sudo apt-get install open-vm-tools open-vm-tools-desktop
```

`$ sudo reboot` .

Check VMware Tools

```bash
lsb_release -a
```

* "Oh My ZSH!"

```bash
sudo apt-get install git zsh curl && sudo chsh -s $(which zsh) && sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

```bash 
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```
Now change content file ~/.zshrc

`$ nano ~/.zshrc` .

```bash
	+) ZSH_THEME="half-life"
	...
	+) plugins=(
		git
	   	zsh-autosuggestions
	   )  
	...
```

> [how-to-make-zsh-the-default-shell](https://askubuntu.com/questions/131823/how-to-make-zsh-the-default-shell) .

```
chsh -s $(which zsh)
```

>Setting Terminal run zsh default: `Preferences/Unnamed/Command/Run a custom command instead of my shell/Custom command: zsh` .

```bash
$ source ~/.zshrc
```

>NOTE: zsh: corrupt history file /home/<user_name>/.zsh_history

zsh often get this error when using

fix:
```bash
$ cd ~ && mv .zsh_history .zsh_history_bad && strings -eS .zsh_history_bad > .zsh_history && fc -R .zsh_history
```

or 

```bash
#!/usr/bin/env zsh
# Fixes a corrupt .zsh_history file

mv ~/.zsh_history ~/.zsh_history_bad
strings -eS ~/.zsh_history_bad > ~/.zsh_history
fc -R ~/.zsh_history
rm ~/.zsh_history_bad
```
Create file bash name `zsh_history_fix` and add into `/usr/bin`.

```bash
chmod +x zsh_history_fix && sudo cp zsh_history_fix /usr/bin && cd ../
```

* Terminator

```bash
sudo apt-get update && sudo apt-get install terminator
```

* Update ubuntu


`$ sudo apt-get update`

### 2) Add i386 architecture (to run file ELF x86 (32-bit))

```bash
sudo dpkg --add-architecture i386
```

### 3) Install Python and Pip

I use both Python2 and Python3 for play Pwn CTFs

From Ubuntu 20.04, py3 is available in base system and py2 is available to install from the Universe repository.

* Python3 and pip3

```bash
sudo apt-get install python3 python3-pip python3-dev
```

```
$ pip3 --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

Upgrade pip3

```bash
python3 -m pip install --upgrade pip
```

* Python2 and pip2

```bash
sudo add-apt-repository universe
```

```bash
sudo apt update && sudo apt install python2 && sudo apt-get install curl && curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py && sudo python2 get-pip.py
```

```bash
$ pip2 --version
pip 20.0.2 from /usr/local/lib/python2.7/dist-packages/pip (python 2.7)
```

NOTE: [Add PATH](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/)

```
# PYTHON write into ~/.bashrc or ~/.zshrc
export PATH="$HOME/bin:/usr/bin/python2:/bin/python2:/usr/bin/python3:/bin/python3:$PATH"

export PATH="$HOME/bin:/usr/local/lib/python2.7/dist-packages/pip:/usr/lib/python3/dist-packages/pip:/home/l1igma_/.local/lib/python3.8/site-packages/pip:/home/l1igma_/.local/bin:$PATH"
```

`source ~/.bashrc` or `source ~/.zshrc`.

### 4) Install needed libraries and support tools

* Update Ubuntu

```bash
sudo apt-get update -y && sudo apt-get upgrade
```

* Install libraries and tools

```bash
sudo apt-get install -y socat build-essential jq strace ltrace curl wget git make procps vim ssh rubygems gcc dnsutils netcat gcc-multilib net-tools gdb gdb-multiarch libssl-dev libffi-dev libpcre3-dev libdb-dev libxt-dev libxaw7-dev libc6:i386 libncurses5:i386 libstdc++6:i386 patchelf elfutils nasm ascii tree
```

`$ reboot` .

* Install python3 libraries

```bash
sudo pip3 install pwntools pathlib2 keystone-engine unicorn capstone ropper ipython
```

```
sudo pip3 install checksec.py
```

* Install python2 libraries

```bash
sudo pip2 install pwntools pathlib2 keystone-engine unicorn capstone ropper ipython
```

### 5) Install Text Editor

You can choose 1 of 2

* [Sublime Text](https://www.sublimetext.com/docs/linux_repositories.html) .

```bash
sudo apt-get install apt-transport-https
```

```bash
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg && echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list && sudo apt-get update && sudo apt-get install sublime-text
```

* [VS Code](https://code.visualstudio.com/download) .

```bash
$ sudo apt update && \
sudo apt install -y software-properties-common apt-transport-https wget  && \
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -  && \
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"  && \
sudo apt update && \
sudo apt install code
```

### 6) Install tools for Pwnable

#### +) Create folder for tools

```bash
cd ~/ && \
mkdir Tools && \
cd Tools
```

(WORKDIR: ~/Tools)

#### +) pwndbg (Gdb extension)

```
sudo apt-get install libc6-dbg libc6:i386 libc6-dbg:i386
```

```bash
git clone https://github.com/pwndbg/pwndbg.git && \
cd pwndbg && \
./setup.sh && \
cd ../
```

FIX ERROR: `sudo apt-get install python3-testresources` .

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

link: [pwninit](https://github.com/io12/pwninit) .

#### +) one_gadget (Tools for one_gadget searching)

```bash
sudo gem install one_gadget
```

link: [one_gadget](https://github.com/david942j/one_gadget) .

#### +) seccomp-tools (Analyze seccomp sandbox in CTF pwn challenges.)

```bash
sudo apt-get install gcc ruby-dev && sudo gem install seccomp-tools
```
link: [seccomp-tools](https://github.com/david942j/seccomp-tools) .

#### +) libc-database

* Use to find version of libc with offset (more libc than web database) .

```bash
git clone https://github.com/niklasb/libc-database && \
cd libc-database && \
sudo apt-get install zstd && \
./get ubuntu && \
cd ../
```

link: [libc-database](https://github.com/niklasb/libc-database) .

or use libc-database search WEB [libc_serach](https://libc.blukat.me/) .

#### +) Docker

* You will need to use docker when you want to setup the same environment with the server .

```bash
sudo apt install -y docker.io && \
sudo apt install -y docker-compose
```

#### +) ROPgadget (Tools for gadget searching)

* It usually install with pwntools, you can pass if you already can use ROPgadget.

>NOTE: pwntools have ROPgadget.

```bash
$ git clone https://github.com/JonathanSalwan/ROPgadget.git && \
cd ROPgadget && \
sudo python3 setup.py install && \
cd ../
```

or

[ROPgadget](https://github.com/JonathanSalwan/ROPgadget)
```
$ sudo apt install python3-pip
$ sudo -H python3 -m pip install ROPgadget
$ ROPgadget --help
```

#### +) radare2

```bash
git clone https://github.com/radare/radare2 && \
cd radare2 && \
sys/install.sh && \
cd ../
```

#### +) Ghidra (Tools for reversing)

* If you cannot run the ghidra, checking the ghidra path again, if it alright, try checking `java` (`jdk` and `jre`)

```bash
sudo apt install -y default-jdk default-jre
```

Or you can use IDA Pro if you have it on your windows host.

* Version 10.1.5 latest in 01/04/2022, check for new version in [ghidra](https://github.com/NationalSecurityAgency/ghidra/releases) .

```bash
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.1.5_build/ghidra_10.1.5_PUBLIC_20220726.zip && \
unzip ghidra_10.1.5_PUBLIC_20220726.zip && \
rm -rf ghidra_10.1.5_PUBLIC_20220726.zip && \
cd ghidra_10.1.5_PUBLIC && \
sudo ln -s ~/Tools/ghidra_10.1.5_PUBLIC/ghidraRun /usr/bin/ghidra && \
cd ../
```

* The command `sudo ln -s ~/Tools/ghidra_10.1.5_PUBLIC/ghidraRun /usr/bin/ghidra` just add the symlink from `ghidraRun` to `/usr/bin/ghidra`, so you can open ghidra with command "ghidra" in terminal

### +) fidra
* Use for dynamic reversing

```
pip3 install frida-tools
```

### 7) Setup qemu

* Use for kernel exploitation or Arm compiler-debug

```bash
sudo apt install -y qemu-user qemu-user-static gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu binutils-aarch64-linux-gnu-dbg && \
sudo apt install -y gcc-arm-linux-gnueabihf binutils-arm-linux-gnueabihf binutils-arm-linux-gnueabihf-dbg && \
sudo apt-get -y install qemu-kvm qemu
```

### 8) Finally

*These are most of the tools I use to play CTF pwn challenges, there are still a lot of other great tools that I haven't used yet. I want to share so that newbies can start on the path of pwnable. After the installation is complete, you should take a snapshot or compress and store it, in case an error occurs. Older or newer versions of Ubuntu will likely have some errors, but basically I think there won't be too much change in the way of installation. Last word, hope you will find passion or pleasure playing pwnable, goodluck.*

------------------------------------------------

### [+] **The article is for general purposes, I recommend that you learn and practice as well as set up tools for the problems you have, do not install all the tools at once and I'm happy to receive your comments.**

### [+] **I keep the advice from the author of the article that I referenced to create this article to thank the author. If the author can read the article, please allow me!!! Thank you very much.**

### [+] NOTE FIX:
+ [echo 20 | sudo tee /proc/sys/kernel/watchdog_thresh](https://www.suse.com/support/kb/doc/?id=000018705) .
