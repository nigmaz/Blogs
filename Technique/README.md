# INTRO
>Tổng hợp lại một số các điểm lưu ý của các kỹ thuật khai thác mà tôi học được và có cả ví dụ code khai thác mẫu đơn giản để luyện tập.

| Technique  | Documents |
|:----------:|:---------:|
|Heap Exploit|        |
|Ret2csu| ✅   |
|Ret2dlresolve|  ✅   |
|SROP| ✅   |
|Stack Pivot| ✅   |

Nếu có gì sai xót rất vui khi nhận sự góp ý từ các bạn ❤❤❤ 

>TrickNote:

* Vậy nên để bypass tránh việc ghi đè canary ta chỉ cần nhập chữ cái (+, -, *, /) mà không thuộc format %lu thì phần tử đó sẽ bị skip, không thay đổi. VD: chall `Warmup` - UIT-2022-CTF . 

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

9. địa chỉ lệnh "ret"
10. địa chỉ nào đó muốn return về.
```

* Use * to have a variable field width, equals to an signed integer on the stack, can combine with positional argument. Eg. %*10$c: print a number of characters equals to the 10th argument. `[FMT XMaster - TTV KCSC 2023]`

* [patchelf](https://github.com/NixOS/patchelf) .

```
$ 
patchelf --set-interpreter ./<ld-[linking dynamic]> --set-rpath ./<libc.so.6-[libc]> ./<my-program>

$ 
patchelf --set-interpreter ./ld-linux-x86-64.so.2 ./chall

patchelf --replace-needed libc.so.6 ./libc.so.6 ./chall
```

* Functions read_str(a1, a2) thường thì sẽ đọc được a2+1 character => offbyone `[The Last One - TTV KCSC 2023]`

* Hàm strncat() sẽ copy chuỗi name vào chuỗi bullet.name, sau đó sẽ thêm 1 ký tự NULL vào cuối chuỗi. => có thể dẫn đến off-by-one => thay đổi size dẫn đến check size bị sai kết quả => bufer overflow vượt qua check size chuỗi đã khởi tạo. 



----------------------------------------------------

[+] Tổng hợp tài liệu để có điểm bắt đầu khi học cho người mới, các lưu ý khai thác của kỹ thuật.

[+] Tổng hợp lại không thay thế được writeup chi tiết, bài báo về kỹ thuật khai thác hay quá trình tự học khai thác của bạn.
