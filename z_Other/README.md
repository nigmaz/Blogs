# Container images, text,... for my Github.

> https://0x434b.dev/

> http://p4nda.top/2018/08/27/WDBCTF-2018/

> https://blog.csdn.net/weixin_52640415/article/details/122599200

> https://wyv3rn.tistory.com/76

> https://wyv3rn.tistory.com/75

> malloc.c full version: https://elixir.bootlin.com/glibc/glibc-2.29/source/malloc/malloc.c

>Pwnable.tw

   * https://hackmd.io/@wxrdnx/r1CXaFHdv
   
   * https://hackmd.io/@ductin/HyGmQq4w9

> TetCTF
 
  * https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiEpLqR7qr9AhUR7GEKHbSBCS0QFnoECAwQAQ&url=https%3A%2F%2Fd4rkn3ss.medium.com%2Fwrite-up-for-pwnable-challenges-tetctf-2019-a74eb177518e&usg=AOvVaw0A1Oieo3lMK_KtxWpRGYcH

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

>Heap

   * https://infosecwriteups.com/heap-exploitation-journey-1-tcache-attack-5b38fb0c19b0

   * https://azeria-labs.com/heap-exploitation-part-2-glibc-heap-free-bins/

   * https://dangokyo.me/2017/12/14/0ctf-2016-quals-pwn-zerostorage-write-up/

   * https://ctf-wiki.mahaloz.re/pwn/linux/glibc-heap/unsorted_bin_attack/

   * https://www.lazenca.net/pages/viewpage.action?pageId=51970214

   * https://lantern.cool/note-pwn-free-hook/#参考

   * https://ctf-wiki.org/pwn/linux/user-mode/environment/

   * https://one2bla.me/the-dark-arts/common-vulnerabilities/unsortedbin-attack.html


