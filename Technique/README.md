# INTRO
>Tổng hợp lại một số các điểm lưu ý của các kỹ thuật khai thác mà tôi học được và có cả ví dụ code khai thác mẫu đơn giản để luyện tập.

| Technique  | Documents |
|:----------:|:---------:|
|Heap Exploit|        |
|Ret2csu| ✅   |
|Ret2dlresolve|  ✅   |
|SROP| ✅   |
|Stack Pivot| ✅   |

>TrickNote:

* [patchelf](https://github.com/NixOS/patchelf) . `TTV KSSC 2023`

```
$ 
patchelf --set-interpreter ./<ld-[linking dynamic]> ./<my-program>

patchelf --set-rpath ./<libc.so.6-[libc]> ./<my-program>

$ 
patchelf --set-interpreter ./ld-linux-x86-64.so.2 ./chall

patchelf --replace-needed libc.so.6 ./libc.so.6 ./chall

         --add-needed
```

## STACK bug.

* Vậy nên để bypass tránh việc ghi đè canary ta chỉ cần nhập chữ cái (+, -, *, /) mà không thuộc format %lu thì phần tử đó sẽ bị skip, không thay đổi. VD: chall `Warmup` - UIT-2022-CTF . 

* Từ Ubuntu 18.04 trở đi, nếu việc thực thi thất bại tại những hàm như buffered_vfprintf() hay do_system() trong những file thực thi 64 bit là do ngay trước câu lệnh ret, đầu vùng nhớ stack được cấp phát 16 bytes cho việc gọi lệnh tại return address nên để thực thi được thì cần chèn thêm 1 ROPgadget "ret" vào trước câu lệnh cần thực thi để bỏ đi 1 stack 8 bytes đầu tiên và thực thi câu lệnh này nằm ở stack ngay sau đó. `pwntools '/bin/sh':`  - next(libc.search(b'/bin/sh')) 

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

* Functions read_str(a1, a2) thường thì sẽ đọc được a2+1 character => offbyone `[The Last One - TTV KCSC 2023]`

* Hàm strncat() sẽ copy chuỗi name vào chuỗi bullet.name, sau đó sẽ thêm 1 ký tự NULL vào cuối chuỗi. => có thể dẫn đến off-by-one => thay đổi size dẫn đến check size bị sai kết quả => bufer overflow vượt qua check size chuỗi đã khởi tạo. `Silver Bullet - pwnable.tw`

## FORMATSTRING bug.

* Use * to have a variable field width, equals to an signed integer on the stack, can combine with positional argument. Eg. %*10$c: print a number of characters equals to the 10th argument. `[FMT XMaster - TTV KCSC 2023]`


* Leak flag (Format String) convert

```python
>>> from pwn import *
>>> f = b''
>>> a = '0x....0x....0x....0x....'
>>> a = a.split('0x')
>>> for i in range(1, len(a)):
>>>   f += p64(int(a[i], 16))
>>> f = ctf{.....}
```

## HEAP EXPLOIT.

* `gdb command in heap:` 
```
      x/40gx &main_arena 
      x/40gx (long long)(&__malloc_hook)-0x80
      set max-visualize-chunk-size 0x500
```

* Unsortedbin Attack - malloc 1 chunk rồi free chunk đó để nó thuộc unsortedbin, khi chunk đó được cấp phát lại - Bây giờ khi một chunk được lấy ra khỏi unsortedbin , một con trỏ để ghi vào đoạn sau của nó [nó ghi con trỏ fd của nó vào bk+0x10 tức là bỏ nó ra khỏi mắt xích rồi nối lại hai mắt xích trước và sau nó với nhau bằng bk và fd]; Cụ thể một con trỏ sẽ được ghi vào `bk + 0x10` trên x64 (`bk + 0x8` cho x86). `Nếu có 1 unsortedbins thì bk và fd của khối đó chỉ về main_arena+88` .

>Sau khi unsortedbins attack thì khối unsortedbins bị set thành corrupted => dễ xảy ra lỗi 

* Fastbin Attack: VD[babyheap - 0ctf 2017] 

(https://medium.com/@thanhtuan9906/0ctf-quals-2017-babyheap-e2638b3e727b)

`Có thể leak bằng fastbins nếu sử dụng ghi đè p8(lastbyte) .`

Cùng là fastbins nhưng [Lưu ý khi dùng fasstbins attack cần set được size của vị trí muốn ghi thỏa mãn là 1 khối chunk fastbin]
```
chunk - 0x20 size thì next chunk lưu ở main_arena+16
                    
chunk - 0x60 size thì next chunk lưu ở main_arena+48 (bài này thì trường hợp này lại exploit thành công).
```

* Để ý các function của chương trình vd chương trình có hàm edit password nghĩa là có thể khi có bug ta sẽ cố gắng khai thác làm sao để free được 1 đoạn nằm trên vị trí password thì sẽ có thể dùng function changePassword để thay đổi dư liệu => Use After Free or Double Free, ... 

## LOGIC bug: seed, permission, ...

* random: dùng seed có giá trị là thời gian thực lúc chạy chương trình, vì vậy tạo 1 script chạy cùng là xong

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

Nhiệm vụ của srand(x) đưa ra seed x rồi rand() dựa vào x đưa ra số a. Khi đó a là seed cho lần gọi rand() tiếp theo (cứ như thế tiếp tục). Do vậy VD trong vòng lặp thời gian 1 giây rand() dùng seed cũ liên tục nên nó không bao giờ ra số khác nhau trong khoảng thời gian đó.

[Meshuggah](https://qbao.home.blog/2020/04/30/start-to-pwnb01lers-ctf/) .

## SECCOMP-tools - SANDBOX 

* [KMACTF2022 - Duet](https://github.com/nhtri2003gmail/CTFWriteup/tree/master/2022/KMACTF-2022/Duet)

* Viết sheelcode cần set context.binary

```python
VD:
exe = context.binary = ELF('./vuln', checksec=False)
...

shellcode = asm('''
         instruction assembly
         ...
''')
```




----------------------------------------------------

[+] Tổng hợp tài liệu để có điểm bắt đầu khi học cho người mới, các lưu ý khai thác của kỹ thuật.

[+] Tổng hợp lại không thay thế được writeup chi tiết, bài báo về kỹ thuật khai thác hay quá trình tự học khai thác của bạn.
