# Ubuntu - Setup VMware for CTF Pwnable challenges .

>DATE: 07/06/2023 - Ubuntu 18.04 | Ubuntu 20.04 | Ubuntu 22.04 .
- `Build file install.sh` is loading...
## [1]. Install "Oh My ZSH!" and VMware Tools

- This is not really to play the pwn CTF challenge but it optimizes your performance when pwning.
- `Turn on ShareFolder VMWARE Ubuntu`.

### 1.1. VMware-Tools

- Check VMware-Tools.

```bash
lsb_release -a && \
sudo snap refresh
```

- Install VMware-Tools.

```bash
sudo apt install open-vm-tools-desktop open-vm-tools && \
reboot
```

- **NOTE**: 

	* Ubuntu 22.04: [How to Fix Drag and Drop Not Working in Ubuntu 22.04 on VMware](https://www.youtube.com/watch?v=y7MQXyjM9Hk).

	```
	$ sudo nano /etc/gdm3/custom.conf 

	#WaylandEnable=false => WaylandEnable=false
	```

	* [Ubuntu 16.04](https://kb.vmware.com/s/article/1022525) .

### 1.2. "Oh My ZSH!"

- Install zsh.

```bash
sudo apt-get install git wget curl zsh -y 
```

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

or

```bash
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

and

```bash
sudo chsh -s $(which zsh) && reboot
```

- Install zsh-autosuggestions.

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

- Now change content file ~/.zshrc.

```bash
$ nano ~/.zshrc
	+) ZSH_THEME="half-life" 
	# or "lukerandall"
	# or "frontcube"
	# or "clean"
	...
	+) plugins=(
		git
	   	zsh-autosuggestions
	   )  
	...
```

- **NOTE:**

    * Run zsh default ~ **[can dropped]**:

	`Preferences/Unnamed/Command/Run a custom command instead of my shell/Custom command: zsh` .
     

    * zsh corrupt history file /home/<user_name>/.zsh_history, fix:

    ```bash
    #!/usr/bin/env zsh
    # Fixes a corrupt .zsh_history file

    mv ~/.zsh_history ~/.zsh_history_bad
    strings -eS ~/.zsh_history_bad > ~/.zsh_history
    fc -R ~/.zsh_history
    rm ~/.zsh_history_bad

    # cd ~ && mv .zsh_history .zsh_history_bad && strings -eS .zsh_history_bad > .zsh_history && fc -R .zsh_history
    ```
    => Create file bash name `zsh_history_fix` and add into `/usr/bin`.

    ```bash
    chmod +x zsh_history_fix && sudo cp zsh_history_fix /usr/bin && cd ../
    ```



### 1.3. Terminator

- DEBUG use Terminator.

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

- **NOTE:** 

    * Not recommend use python2 and pip2 `[exploitation kernel tools pip2 error]`.
	
    * Should use python3 install new versions or use direct python3 in OS Ubuntu.

### 3.1. Python3 new version (not use directly python OS)

- [Python3 install new versions](https://github.com/nigmaz/Blogs/blob/main/Virtual-Machine/Ubuntu/config.md#13-python3-new-versions) .
- [Python 3.10 - Ubuntu 18.04 and 20.04 LTS | Video](https://www.youtube.com/watch?v=q_SDagn_740) .

### 3.2. Python3 and pip3 (use directly in OS Ubuntu)

```bash
sudo apt-get install python3 python3-dev python3-pip && \
pip3 --version
```

- Upgrade pip3 (Add PATH => Upgrade pip3)

```bash
python3 -m pip install --upgrade pip
```

- Error (pip or lib not support python3 less version)
    * [Upgrade python3 in ubuntu 18.04](https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-10-on-ubuntu-18-04-and-20-04-lts/) .
    * [Upgrade python latest version in ubuntu](https://cloudbytes.dev/snippets/upgrade-python-to-latest-version-on-ubuntu-linux) .

```bash
sudo apt remove python3-pip 
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```

### 3.3. Python2 and pip2 (Not recommended)

```bash
sudo add-apt-repository universe && \
sudo apt update && sudo apt install python2 && \
sudo apt-get install curl && \
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py && \
sudo python2 get-pip.py && \
pip2 --version
# pip 20.0.2 from /usr/local/lib/python2.7/dist-packages/pip (python 2.7)
```

### 3.4. **NOTE:**

- [Add PATH](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/)

```
# PYTHON write into ~/.bashrc or ~/.zshrc
export PATH="$HOME/bin:/usr/bin/python3:/usr/bin/pip3:/usr/lib/python3/dist-packages/pip:/home/nigmaz/.local/bin:$PATH"

# export PATH="$HOME/bin:/usr/bin/python3:/bin/python3/usr/lib/python3/dist-packages/pip:/home/nigma/.local/lib/python3.8/site-packages/pip:/home/nigma/.local/bin:/usr/local/lib/python3.8/dist-packages:$PATH"
# export PATH="$HOME/bin:/usr/bin/python2:/bin/python2:/usr/local/lib/python2.7/dist-packages/pip:$PATH"
# cat /etc/environment
# echo $PATH
```

=> `source ~/.bashrc` or `source ~/.zshrc`.

## [4]. Install Libraries and support Tools

- Update Ubuntu.

```bash
sudo apt-get update -y && sudo apt-get upgrade
```

### 4.1. Install Tools

```bash
sudo apt-get install -y socat build-essential jq strace ltrace curl wget git make procps vim ssh rubygems gcc dnsutils netcat gcc-multilib net-tools gdb gdb-multiarch libssl-dev libffi-dev libpcre3-dev libdb-dev libxt-dev libxaw7-dev libc6 libncurses5 libstdc++6 patchelf elfutils nasm ascii tree
```

### 4.2. Install Python3 Libraries

```bash
python3 -m pip install pwntools pathlib2 keystone-engine unicorn capstone ropper ipython
```

- __NOTE:__ Fix in VPS: 
	* sudo apt-get install python3-setuptools
	* pip3 install setuptools-rust

### 4.3. Install Python2 Libraries

```bash
python2 -m pip install pwntools pathlib2 keystone-engine unicorn capstone ropper ipython
```

## [5]. Install Text Editor

- You can choose 1 of 2

### 5.1. [Sublime Text](https://www.sublimetext.com/docs/linux_repositories.html)

```bash
sudo apt-get install apt-transport-https && \
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg && echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list && sudo apt-get update && sudo apt-get install sublime-text
```

### 5.2. [VS Code](https://code.visualstudio.com/download)

- [Reference-VScodeInstall](https://www.makeuseof.com/how-to-install-visual-studio-code-ubuntu/)

```bash
sudo apt update && \
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

( **WORKDIR:** ~/Tools | or **use directly ~/Public** ).

### 6.2. Plugin debug (Gdb extension)

- After `git clone` and use `git checkout <version>`.
```bash
git clone https://github.com/pwndbg/pwndbg && cd pwndbg && \
./setup.sh && cd ../
```

- Fix pip install.

```
sudo apt-get install libc6-dbg libc6 libc6-dbg:i386 libc6:i386 && \
sudo apt-get install python3-testresources
```

- Fix __AttributeError: module 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'__ in wsl

```bash
python3 -m pip install pip --upgrade &&
python3 -m pip install pyopenssl --upgrade
```

- Plugin-gdb - [Template](https://github.com/nigmaz/Blogs/blob/main/Virtual-Machine/Ubuntu/config.md#14-gdbinit):

    * [pwndbg](https://github.com/pwndbg/pwndbg) .

    * [gef](https://github.com/hugsy/gef) .
    ```bash
    git clone https://github.com/hugsy/gef.git
    echo source `pwd`/gef/gef.py >> ~/.gdbinit
    ```

    * [gdb-peda](https://github.com/longld/peda) .

>You can use 3 plugin in 1 OS [Reference all-for-one](https://infosecwriteups.com/pwndbg-gef-peda-one-for-all-and-all-for-one-714d71bf36b8) . 

### 6.3. [pwninit](https://github.com/io12/pwninit) (Tools Patching Libc)

- Download the pwninit binary and copy to `/usr/bin/` to excute as a command in terminal.

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

- Use to find version of libc with offset (more libc than web database).

```bash
git clone https://github.com/niklasb/libc-database && \
cd libc-database && \
sudo apt-get install zstd && \
./get ubuntu && \
cd ../
```

or use libc-database search WEB [libc_serach](https://libc.blukat.me/).

### 6.7. Docker

- You will need to use docker when you want to setup the same environment with the server.

```bash
sudo apt install -y docker.io && \
sudo service docker status
```

- `docker-compose`: https://www.educative.io/blog/docker-compose-tutorial

- References:
  - https://docs.docker.com/engine/install/ubuntu/
  - https://docs.docker.com/compose/install/standalone/

### 6.8. IDA Freeware (Tools for reversing)

**NOTE:** `sudo apt-get install libxcb-xinerama0` .

- [Download IDA](https://hex-rays.com/ida-pro/).

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

- **Save file this as "ida64.desktop" in folder ~/.local/share/applications**.

- [Youtube Tutorial](https://www.google.com/search?q=how+to+install+ida+freeware+on+ubuntu&biw=1536&bih=758&tbm=vid&sxsrf=ALiCzsbb55gpcDfE0SMX5cbXcN5cGbliDQ%3A1669274367537&ei=_xp_Y9WqINqi-Qbg9bqgBg&oq=h%C6%A1+to+install+ida+for+ubuntu&gs_lcp=Cg1nd3Mtd2l6LXZpZGVvEAMYAjIECCMQJzIGCAAQFhAeMgYIABAWEB4yBggAEBYQHlAAWABg9RBoAHAAeACAAXKIAXKSAQMwLjGYAQDAAQE&sclient=gws-wiz-video#fpstate=ive&vld=cid:caa36be6,vid:3FnyzJ6bTEs).

### 6.9. Ghidra (Tools for reversing)

- If you cannot run the ghidra, checking the ghidra path again, if it alright, try checking `java` (`jdk` and `jre`).

```bash
sudo apt install -y default-jdk default-jre
```

- Version 10.1.5 latest in 01/04/2022, check for new version in [ghidra](https://github.com/NationalSecurityAgency/ghidra/releases).

```bash
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.1.5_build/ghidra_10.1.5_PUBLIC_20220726.zip && \
unzip ghidra_10.1.5_PUBLIC_20220726.zip && \
rm -rf ghidra_10.1.5_PUBLIC_20220726.zip && \
cd ghidra_10.1.5_PUBLIC && \
sudo ln -s ~/Public/ghidra_10.1.5_PUBLIC/ghidraRun /usr/bin/ghidra && \
cd ../
```

- The command `sudo ln -s ~/Tools/ghidra_10.1.5_PUBLIC/ghidraRun /usr/bin/ghidra` just add the symlink from `ghidraRun` to `/usr/bin/ghidra`, so you can open ghidra with command "ghidra" in terminal.

### 6.10. Radare2

```bash
git clone https://github.com/radare/radare2 && \
cd radare2 && \
sys/install.sh && \
cd ../
```

### 6.11. Fidra

- Use for dynamic reversing.

```
pip3 install frida-tools
```

### 6.12. FSOP - add libc source code to GDB

- Use when you want to debug deep in libc function like (printf, puts, read, ...), i need to setup this when i learned FSOP attack.

- Download the glibc source code.

```bash
git config --global http.sslverify false && \
git clone https://sourceware.org/git/glibc.git
```

- Setup some scripts for convenient work.

```bash
mkdir add_glibc_source && \
cd add_glibc_source && \
touch add_glibc_source.py && \
nano add_glibc_source.py
```

- Copy and patse this code to `add_glibc_source.py`, edit the path `/home/nigmaz/` to your path ( this is my scripts, sorry if it so noob :) ).

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

add_all_folder('/home/nigmaz/Public/glibc/')
```

- We add this script to `.gdbinit`, this will auto add glibc source code when we start gdb.

```bash
echo "source ~/Public/add_glibc_source/add_glibc_source.py" >> ~/.gdbinit
```

- Create another scripts.

```bash
touch libc && \
nano libc
```

- Copy and patse this code to `libc`.

```bash
#!/bin/sh

cd ~/Public/glibc/
git checkout release/$1/master
```

- Add it to `/usr/bin/` to execute as a command.

```bash
chmod +x libc && \
sudo cp libc /usr/bin && \
cd ../
```

- Later if you want to change version of glibc source code, just open the terminal and type `libc + version`, this equal to go to the libc folder and checkout to that version.

### 6.13. Setup qemu 

- `Kernel Exploitation compiler-debug`.

```bash
sudo apt-get install git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison qemu-utils qemu-system-x86
```

- Exploit kernel challenge remote, you need compile exploit file small size.

```bash
sudo apt-get install musl-tools
```

- `ARM Exploitation compiler-debug`:
  	* https://github.com/nigmaz/Blogs/tree/main/Pwnable-Technique/ARM%20Exploit

- Tổng hợp

```bash
sudo apt install -y qemu-user qemu-user-static gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu binutils-aarch64-linux-gnu-dbg && \
sudo apt install -y gcc-arm-linux-gnueabihf binutils-arm-linux-gnueabihf binutils-arm-linux-gnueabihf-dbg && \
sudo apt-get -y install qemu-kvm qemu
```

### 6.14. Metasploit Framework

- https://linuxways.net/ubuntu/how-to-install-metasploit-framework-on-ubuntu-20-04/

# [7]. Finally

- **The article is for general purposes, I recommend that you learn and practice as well as set up tools for the problems you have, do not install all the tools at once and I'm happy to receive your comments.**

- **For me, this series serves as a reminder, an exploitation template for me to look back on and reuse in the future, but if it could help someone on their first steps into Linux exploitation for just a little bit, I would be very delighted.**

>WELL!!!

*These are most of the tools I use to play CTF pwn challenges, there are still a lot of other great tools that I haven't used yet. I want to share so that newbies can start on the path of pwnable. After the installation is complete, you should take a snapshot or compress and store it, in case an error occurs. Older or newer versions of Ubuntu will likely have some errors, but basically I think there won't be too much change in the way of installation. Last word, hope you will find passion or pleasure playing pwnable, goodluck.*


