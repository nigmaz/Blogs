# 1) Compile secure flag
>gcc file.c -o file | gcc -Wl,-z,relro -fno-stack-protector -no-pie

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

### Other:
- `-m32` biên dịch file 32 bit ; không để gì là biên dịch file 64 bit.
- `-s` : thuộc tính `stripped` - Xóa tất cả `symbol table` và `relocation information` khỏi tệp thực thi.
- `-static` : file không liên kết thư viện động.
- `-g` : debug file with source code.

### Make: use cmd linux `make` compile filename Makefile contain cmd build program.

```
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

# 2) GDB truyền đối số hoặc dữ liệu
```
Khi nhận được giá trị đầu vào sau khi chạy chương trình, gdb có thể truyền giá trị như sau.

gef➤  r <<< $(perl -e 'print "%n"')
Starting program: /challenge/app-systeme/ch17/ch17 <<< $(perl -e 'print "%n"')
Ngoài ra, bạn có thể tạo một tệp chứa các giá trị đầu vào và tải nó khi chương trình được chạy.

gef➤  r < input.tx
Ngoài ra, có một cách để tạo một tệp tạm thời và tải lại tệp, như hình dưới đây, nhưng nó không chắc sẽ được sử dụng.

gef➤  r `perl -e 'print "A"x10' > tmp` < tmp
```

-------------------------------------------------

[+] https://dtrugman.medium.com/elf-loaders-libraries-and-executables-on-linux-e5cfce318f94

[+] https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro
