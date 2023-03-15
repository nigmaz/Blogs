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

# 2) GDB truyền đối số hoặc dữ liệu
```
Khi nhận được giá trị đầu vào sau khi chạy chương trình, gdb có thể truyền giá trị như sau.

gef➤  r <<< $(perl -e 'print "%n"')
Starting program: /challenge/app-systeme/ch17/ch17 <<< $(perl -e 'print "%n"')
Ngoài ra, bạn có thể tạo một tệp chứa các giá trị đầu vào và tải nó khi chương trình được chạy.

gef➤  r < 파일명
Ngoài ra, có một cách để tạo một tệp tạm thời và tải lại tệp, như hình dưới đây, nhưng nó không chắc sẽ được sử dụng.

gef➤  r `perl -e 'print "A"x10' > tmp` < tmp
```

-------------------------------------------------

[+] https://dtrugman.medium.com/elf-loaders-libraries-and-executables-on-linux-e5cfce318f94

[+] https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro
