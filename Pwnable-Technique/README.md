# Pwnable-Technique

> Tổng hợp kỹ thuật khai thác và có ví dụ khai thác mẫu đơn giản để luyện tập trong quá trình chơi CTF.

- Hiểu rõ các lý thuyết máy tính cơ bản như `Mạng máy tính`, `Hệ điều hành`, `Kiến trúc máy tính` và `Lý thuyết trình biên dịch` là bốn lý thuyết máy tính cơ bản quan trọng nhất 
và hầu như tất cả các kỹ thuật mới đều được xây dựng dựa trên bốn lý thuyết này.
- TARGET:
   * Heap and Other House of Heap...
   * Heap v2.0
   * FSOP fake vtable-2.27
   * Side Chanel Attack
   * Fuzzing
   * ARM Exploit
   * Begin Windows Exploit
   * ...
## [0]. Cheatsheet

- [GLIBC source code](https://elixir.bootlin.com/glibc/glibc-2.23/source) .
- [Problem when exploit remote with socat](https://ir0nstone.gitbook.io/notes/types/stack/exploiting-over-sockets/socat) .

- `pwntools` - [pwntools-cheatsheet.md](https://gist.github.com/anvbis/64907e4f90974c4bdd930baeb705dedf) .
    * Challenge stripped và Enable PIE:
        + gdb.attach() sử dụng `breakrva [offset]`
        + Check giá trị biến toàn cục thì `got` -> tìm dần lên theo địa chỉ của GOT được lưu.
    * Sample python script
    ```python
    #!/usr/bin/env python3
    from pwn import *

    elf = ELF("./babyheap")
    # p = process('./unexploitable',env={'LD_PRELOAD' :'./libc.so.6'}) 
    libc = ELF("/usr/lib/x86_64-linux-gnu/libc.so.6")
    ld = ELF("/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2")
    if args.LOCAL:
        p = elf.process()
        if args.GDB:
            context.update(binary=elf, log_level="DEBUG")
            gdb.attach(
                p,
                """
                
                """,
            )
    else:
        p = remote("", "")

    p.interactive()
    ```

- `GDB` .
    * Arguments
    ```bash
    gdb -q --args ./babyrev_2 111111111111111ABCDEFGHIJKMNTO
    ```
    * GDB khi nhận giá trị đầu vào là kết quả của chương trình khác.
    ```bash
    gef➤  r <<< $(perl -e 'print "%n"')
    Starting program: /challenge/app-systeme/ch17/ch17 <<< $(perl -e 'print "%n"')

    Ngoài ra, bạn có thể tạo một tệp chứa các giá trị đầu vào và tải nó khi chương trình được chạy.
    gef➤  r < input.tx

    Ngoài ra, có một cách để tạo một tệp tạm thời và tải lại tệp, như hình dưới đây, nhưng nó không chắc sẽ được sử dụng.
    gef➤  r `perl -e 'print "A"x10' > tmp` < tmp
    ```

- `core dump` .

    * Check field `-c: core file size` , if this unable
        + Use `ulimit -c unlimited`
        + Or auto enable core-dump, `nano /etc/security/limits.conf` and edit `<user>      hard    core        ulimited` .
    ```bash
    ulimit -a
    ```
    
    * Check path store core file
    ```bash
    cat /proc/sys/kernel/core_pattern
    ```

    * Go to path file get file core-dump

    ```bash
    gdb -q <file>
    (gdb) core <path-core-file>
    ```

- `patchelf` - Patch Glibc into elf.
```bash
##################### SUGGEST ##########################
$ patchelf --set-interpreter ./ld-linux-x86-64.so.2 ./chall
$ patchelf --replace-needed libc.so.6 ./libc.so.6 ./chall

########################################################
$ patchelf --set-interpreter ./<ld-[linking dynamic]> ./<my-program>
$ patchelf --set-rpath ./<libc.so.6-[libc]> ./<my-program>
=> patchelf --set-interpreter ld.so --set-rpath . chall

############### parameter ############################## 
$ check use: --print-needed
$        --add-needed
```

- `google-colab` trong 1 số trường hợp đặc biệt (tăng tốc độ kết nối đến server).

```python
!pip install pyelftools==0.28
!pip install pwntools==4.7.1
import os
os.environ['PWNLIB_NOTERM'] = '1'
os.environ['JUPYTER_DETECTED'] ='yes'
from google.colab import drive
drive.mount('/content/drive')
!ls
%cd /content/drive/MyDrive/Colab Notebooks/
!ls -al
#!/usr/bin/env python3
from pwn import *
< ... script-pwntools ... >
```

## [1]. Compile use mitigations
 
### RELRO:
- Partial RELRO: `-Wl,-z,relro`
- Full RELRO: `-Wl,-z,relro,-z,now`

### CANARY:
- No canary found : `-fno-stack-protector`
- Canary found: `-fstack-protector-all`

### NX: 
- Tắt: `-z execstack`
- Bật: Tự động bật

### Pie:
- No pie: `-no-pie`
- Pie enable: `-pie -fpie`

### Other: https://linuxhandbook.com/gcc-flags/
- `-m32` biên dịch file 32 bit ; không để gì là biên dịch file 64 bit.
- `-s` : thuộc tính `stripped` - Xóa tất cả `symbol table` và `relocation information` khỏi tệp thực thi.
- `-static` : file không liên kết thư viện động.
- `-g` : debug file with source code.
- `-Wall` : in ra mọi warning để tạo mã tốt nhất có thể.

## [2]. Refenrences:

[+] https://dtrugman.medium.com/elf-loaders-libraries-and-executables-on-linux-e5cfce318f94

[+] https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro

[+] `Pwnable Map`
   * `[1]` Stack bug.
   * `[2]` Format string.
   * `[3]` Heap bug.
   * `[4]` FileStructure attack.
   * `[5]` Race condition.
   * `[6]` Typeof Confusion.
   * `[7]` Integer Overflow.
   * `[8]` Logic bug.
   * `[9]` Sandbox Escape.
   * `[10]` *Linux Kernel. (Kernel read CVE Pwn2Own => report modern and variant hunting)
   * `[11]` *ARM Exploit.
   * `[12]` *Windows Exploit.
   * `[13]` *Browser Exploit. (Browser v8 pwn => state of the art exploit)
   * `[14]` *CVE realworld. (RCE&PLE => Windows | Linux | IOS)
