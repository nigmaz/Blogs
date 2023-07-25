# Pwnable-Technique

> Tổng hợp kỹ thuật khai thác và có ví dụ khai thác mẫu đơn giản để luyện tập trong quá trình chơi CTF.

- Hiểu rõ các lý thuyết máy tính cơ bản như Mạng máy tính, Hệ điều hành, Kiến trúc máy tính và Lý thuyết trình biên dịch là bốn lý thuyết máy tính cơ bản quan trọng nhất 
và hầu như tất cả các kỹ thuật mới đều được xây dựng dựa trên bốn lý thuyết này.

   * [1] Stack bug.

   * [2] Format string.

   * [3] Heap bug.

   * [4] IO-File Structure.

   * [5] Race condition.

   * [6] Typeof Confusion.

   * [7] Integer Overflow.

   * [8] Sandbox Escape.

   * [9] Linux Kernel. (Kernel read CVE => report => modern hơn | kernel Pwn2Own - đọc CVE xong variant hunting)

   * [10] ARM - Pwn.

   * [11] Pwn - Windows.

   * [12] Browser Serach (Browser v8 pwn - state of the art exploit)

   * [13] CVE realworld (RCE/PLE - Windows | Linux | IOS)

## [0]. Cheatsheet

- [g-libc source](https://elixir.bootlin.com/glibc/glibc-2.23/source) .
- [Video list Temple Of Pwn](https://www.youtube.com/watch?v=TqGMVRV2l9s&list=PLiCcguURxSpbD9M0ha-Mvs-vLYt-VKlWt) .
- [Vấn đề khi khai thác remote với socat](https://ir0nstone.gitbook.io/notes/types/stack/exploiting-over-sockets/socat) .

- Với những bài bị stripped và bật PIE => gdb.attach sử dụng `breakrva *[offset]`, check giá trị biến toàn cục thì `got` -> tìm dần lên theo địa chỉ của GOT được lưu.

- pwntools hỗ trợ flat(...) giá trị byte điền tự động là p64() hoặc p32() phụ thuộc cấu trúc chương trình là x86 hay x86_64 hoặc có thể đặt giá trị giống code exploit `[convert - ASCIS 2022]` .

- Patchelf LIBC or pwnint 
```bash
##################### SUGGEST #########################
$ patchelf --set-interpreter ./ld-linux-x86-64.so.2 ./chall
$ patchelf --replace-needed libc.so.6 ./libc.so.6 ./chall


$ patchelf --set-interpreter ./<ld-[linking dynamic]> ./<my-program>
$ patchelf --set-rpath ./<libc.so.6-[libc]> ./<my-program>

############### parameter ############################## 
$ check use: --print-needed
$        --add-needed

python script load: p = process('./unexploitable',env={'LD_PRELOAD' :'./libc.so.6'}) 
```

- GDB Khi nhận được giá trị đầu vào sau khi chạy chương trình, gdb có thể truyền giá trị như sau.

```bash
gef➤  r <<< $(perl -e 'print "%n"')
Starting program: /challenge/app-systeme/ch17/ch17 <<< $(perl -e 'print "%n"')
Ngoài ra, bạn có thể tạo một tệp chứa các giá trị đầu vào và tải nó khi chương trình được chạy.

gef➤  r < input.tx
Ngoài ra, có một cách để tạo một tệp tạm thời và tải lại tệp, như hình dưới đây, nhưng nó không chắc sẽ được sử dụng.

gef➤  r `perl -e 'print "A"x10' > tmp` < tmp
```

- Sử dụng google-colab trong 1 số trường hợp đặc biệt.

```python
!pip install --upgrade git+https://github.com/Gallopsled/pwntools.git
import os
os.environ['PWNLIB_NOTERM'] = '1'
os.environ['JUPYTER_DETECTED'] ='yes'
from google.colab import drive
drive.mount('/content/drive')
!ls
%cd /content/drive/MyDrive/Colab Notebooks/
!ls
...script-pwntools
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


### Make: use cmd linux `make` compile filename Makefile contain cmd build program.

```bash
EXAMPLES
Example-1:

To Build your programs:

$ make

output:

 gcc -c -Wall test1.c
 gcc -c -Wall test2.c
 gcc -Wall test1.o test2.o -o test 

Note: make reads makefile present in current directory and executes based on statements in makefile
Example-2:

To clean all the object files:

$ make clean

output:

 rm -rf *.o test
Example-3:

 To forcibly build all programs, use -B option:

$ make -B

output:

 gcc -c -Wall test.c
 gcc -c -Wall anotherTest.c
 gcc -Wall test.o anotherTest.o -o test
Example-4:

To run make in debug mode, use the -d option :

$ make -d

output:

Copyright (C) 2006 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
This program built for x86_64-pc-linux-gnu

Reading makefiles...
Reading makefile `Makefile'...
Updating makefiles....
Considering target file `Makefile'.
Looking for an implicit rule for `Makefile'.
Trying pattern rule with stem `Makefile'.
Trying implicit prerequisite `Makefile.o'.
Trying pattern rule with stem `Makefile'.
Trying implicit prerequisite `Makefile.c'.
Trying pattern rule with stem `Makefile'.
Trying implicit prerequisite `Makefile.cc'.
Trying pattern rule with stem `Makefile'.
Trying implicit prerequisite `Makefile.C'.
Trying pattern rule with stem `Makefile'.
Trying implicit prerequisite `Makefile.cpp'.
Trying pattern rule with stem `Makefile'.
--More--
Example-5:

To build programs present in different directory:

$ make -C /home/testdir/

output:

make: Entering directory `/home/himanshu/practice/make-dir'
make: Nothing to be done for `all'.
make: Leaving directory `/home/himanshu/practice/make-dir'
Example-6:

To use other file instead of default makefile, use -f option :

$ make -f my_makefile

output:

gcc -c -Wall test1.c
gcc -c -Wall test2.c
gcc -Wall test1.o test2.o -o test 
```

## [2]. Refenrences:

[+] https://dtrugman.medium.com/elf-loaders-libraries-and-executables-on-linux-e5cfce318f94

[+] https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro
