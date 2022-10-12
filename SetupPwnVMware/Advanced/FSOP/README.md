# Add libc source code to gdb


* Use when you want to debug deep in libc function like (printf, puts, read, ...), i need to setup this when i learned FSOP attack

* Download the glibc source code (workdir: Tools)

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

* Copy and patse this code to `add_glibc_source.py`, edit the path `/home/<username>/` to your path.

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

add_all_folder('/home/l1igma/Tools/glibc/')
```

* We add this script to `~/.gdbinit`, this will auto add glibc source code when we start gdb

```bash
$ echo "source ~/Tools/add_glibc_source/add_glibc_source.py" >> ~/.gdbinit
```

* Create another scripts

```bash
touch libc && \
nano libc
```

* Copy and patse this code to `libc`

```bash
#!/bin/sh

cd ~/Tools/glibc/
git checkout release/$1/master
```

* Add it to `/usr/bin/` to execute as a command

```bash
chmod +x libc && \
sudo cp libc /usr/bin && \
cd ../
```

* Later if you want to change version of glibc source code, just open the terminal and type `libc + version`, this equal to go to the libc folder and checkout to that version .
