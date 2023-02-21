# Container images, text,... for my Github.

https://hackmd.io/@wxrdnx/r1CXaFHdv

```python 
#!/usr/bin/env python3 
ptr = 0x603100

from pwn import *

elf = ELF('./vuln')
libc = ELF('./libc.2.23.so')
context.log_level = 'DEBUG'

p = elf.process()
gdb.attach(p, '''

''')

def register(name, passwd):
    p.sendafter(b'> ', b'1')
    p.sendafter(b'username\n> ', name)
    p.sendafter(b'password\n> ', passwd)
    p.sendafter(b'password\n> ', passwd)

def login(name, passwd):
    p.sendafter(b'> ', b'2')
    p.sendafter(b'username\n> ', name)
    p.sendafter(b'password\n> ', passwd)


def info(username, password):
    p.sendlineafter(b'> ', b'1')
    p.sendafter(b'username\n> ', username)

def send(username, money):
    p.sendlineafter(b'> ', b'2')
    p.sendafter(b'to?\n', username)
    p.sendlineafter(b'many?\n', str(money).encode())

def view_trans():
    p.sendlineafter(b'> ', b'3')

def change_passwd(password):
    p.sendlineafter(b'> ', b'4')
    p.sendafter(b'password\n> ', password)

def delete():
    p.sendlineafter(b'> ', b'5')

def logout():
    p.sendlineafter(b'> ', b'6')






p.interactive()

```

https://azeria-labs.com/heap-exploitation-part-2-glibc-heap-free-bins/

https://dangokyo.me/2017/12/14/0ctf-2016-quals-pwn-zerostorage-write-up/

https://ctf-wiki.mahaloz.re/pwn/linux/glibc-heap/unsorted_bin_attack/

https://www.lazenca.net/pages/viewpage.action?pageId=51970214

https://lantern.cool/note-pwn-free-hook/#参考

https://ctf-wiki.org/pwn/linux/user-mode/environment/

https://one2bla.me/the-dark-arts/common-vulnerabilities/unsortedbin-attack.html


