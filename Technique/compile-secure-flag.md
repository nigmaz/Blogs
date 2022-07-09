# Compile secure flag

### RELRO:
- Partial RELRO: -Wl,-z,relro
- Full RELRO: -Wl,-z,relro,-z,now

### CANARY:
- No canary found : -fno-stack-protector
- Canary found: -fstack-protector-all

### NX: 
- Tắt: -z execstack
- Bật: Tự động bật

### Pie:
- No pie: -no-pie
- Pie enable: -pie -fpie

### Other:
- -m32 biên dịch file 32 bit ; không để gì là biên dịch file 64 bit.
- -s : thuộc tính `stripped` - Xóa tất cả `symbol table` và `relocation information` khỏi tệp thực thi.
- -static : file không liên kết thư viện động.
- -g : debug file with source code.
-------------------------------------------------

[+] https://dtrugman.medium.com/elf-loaders-libraries-and-executables-on-linux-e5cfce318f94

[+] https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro
