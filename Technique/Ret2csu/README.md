# Ret2csu

>Được sử dụng khi muốn kiếm soát giá trị các thanh ghi nhưng thiếu các `gadget` cần thiết (Đặc biệt là với thanh ghi `rdx`).

Đối với việc khai thác chương trình 64bit, do `The __fastcall calling convention` mà các đối số khi gọi hàm sẽ được lưu trên các thanh ghi lần lượt là rdi, rsi, rdx, rcx, r8, r9 và sau đó mới đến stack. Vì vậy việc kiểm soát các giá trị của các thanh ghi rất quan trọng.

Thường thì chương trình sẽ xuất hiện 2 gadget cho phép kiểm soát rdi và rsi:

- pop rdi ; ret

- pop rsi ; pop r15 ; ret

Nhưng bắt đầu từ việc kiểm soát thanh ghi đối số thứ ba là `rdx` trở đi, mọi chuyện trở nên khó khăn hơn. Nhất là khi khai thác, ta muốn leak một địa chỉ nào đó bằng hàm `write` hoặc viết vào đâu đó bằng hàm `read` đã được liên kết động với chương trình - hai hàm trên đều yêu cầu ba đối số khi gọi hàm.

Giải pháp là chúng ta sẽ tận dụng hàm `__libc_csu_init` được liên kết vào chương trình khi biên dịch động chương trình với thư viện được liên kết. Hàm này có một số đoạn mã như sau có thể tận dụng được.

```asm
pop rbx
pop rbp
pop r12
pop r13
pop r14
pop r15
ret
```

và 

```asm
mov rdx, r14
mov rsi, r13
mov edi, r12d
call QWORD PTR [r15+rbx*8]
```

Gadget thứ hai không giống sẽ có thể sử dụng được do không có `ret` để nối gadget nhưng `call QWORD PTR [r15+rbx*8]` gọi tới hàm có địa chỉ được lưu tại vị trí `r15+rbx*8` mà gadget 1 cho phép chúng ta kiểm soát r15 va rbx nên ta vẫn có thể tính toán được.

>Note: ta sẽ thiết lập rbx = 0 để có thể dễ dàng tính toán khi mà nơi được gọi đến chỉ còn phụ thuộc vào r15. Lúc này ta chỉ còn phải tìm là `một địa chỉ bộ nhớ chứa nơi chúng ta muốn nhảy đến`.

Bây giờ chúng ta có thể kiểm soát được giá trị trên thanh ghi `rdx` và `rsi` thông qua `r14 và r13`, sau đó nhảy về nơi ta muốn chương trình tiếp tục thực thi bằng cách kiểm soát giá trị trên `r15` và `rbx`.

=> Điều này thực sự rất hữu ích khi ta muốn dùng nó phục vụ cho các syscall như `execve` hoặc là điền tham số các hàm như `write` và `read`.

Tổng quát hơn nó sẽ trông như thế này.

Gadgets are:

|    popper   |    caller         |
| ----------- | ----------------- |
| pop rbx     | mov    rdx, r13   |
| pop rbp     | mov    rsi, r12   |
| pop r12     | mov    edi, ebp   |
| pop r13     | call qword ptr [r15 + rbx*0x8] |
| pop r14     | 
| pop r15     |
| ret         |

>VD:

```asm
   0x00000000004011b0 <+0>:	endbr64 
   0x00000000004011b4 <+4>:	push   r15
   0x00000000004011b6 <+6>:	lea    r15,[rip+0x2c53]        # 0x403e10
   0x00000000004011bd <+13>:	push   r14
   0x00000000004011bf <+15>:	mov    r14,rdx
   0x00000000004011c2 <+18>:	push   r13
   0x00000000004011c4 <+20>:	mov    r13,rsi
   0x00000000004011c7 <+23>:	push   r12
   0x00000000004011c9 <+25>:	mov    r12d,edi
   0x00000000004011cc <+28>:	push   rbp
   0x00000000004011cd <+29>:	lea    rbp,[rip+0x2c44]        # 0x403e18
   0x00000000004011d4 <+36>:	push   rbx
   0x00000000004011d5 <+37>:	sub    rbp,r15
   0x00000000004011d8 <+40>:	sub    rsp,0x8
   0x00000000004011dc <+44>:	call   0x401000 <_init>
   0x00000000004011e1 <+49>:	sar    rbp,0x3
   0x00000000004011e5 <+53>:	je     0x401206 <__libc_csu_init+86>
   0x00000000004011e7 <+55>:	xor    ebx,ebx
   0x00000000004011e9 <+57>:	nop    DWORD PTR [rax+0x0]
   0x00000000004011f0 <+64>:	mov    rdx,r14    ############################################
   0x00000000004011f3 <+67>:	mov    rsi,r13
   0x00000000004011f6 <+70>:	mov    edi,r12d
   0x00000000004011f9 <+73>:	call   QWORD PTR [r15+rbx*8]  ; sau khi gọi hàm với các đối số đã được thiết lập gadget chạy xuống dòng dưới.
   0x00000000004011fd <+77>:	add    rbx,0x1
   0x0000000000401201 <+81>:	cmp    rbp,rbx
   0x0000000000401204 <+84>:	jne    0x4011f0 <__libc_csu_init+64>
   0x0000000000401206 <+86>:	add    rsp,0x8                 ; để ý dòng này để set "A" * 8 nhằm tương thích với instruction để không bị chèn sai giá trị thanh ghi.
   0x000000000040120a <+90>:	pop    rbx        ############################################
   0x000000000040120b <+91>:	pop    rbp
   0x000000000040120c <+92>:	pop    r12
   0x000000000040120e <+94>:	pop    r13
   0x0000000000401210 <+96>:	pop    r14
   0x0000000000401212 <+98>:	pop    r15
   0x0000000000401214 <+100>:	ret 
```

>Tôi học được nó khi mà muốn cố gắng setup giá trị thanh ghi rdx để sử dụng `write` cho việc leak giá trị của `linkmap` phục vụ cho khai thác `ret2dlresolve` trên kiến trúc 64bit.

>NOTE: Có một vài trường hợp kết hợp nó với gadget sau để cộng vào một giá trị bất kỳ do `rbp` và `rbx` đều do ta kiểm soát.

```bash
   0x4013ca <__libc_csu_init+90>:       pop    rbx
   0x4013cb <__libc_csu_init+91>:       pop    rbp
   0x4013cc <__libc_csu_init+92>:       pop    r12
   0x4013ce <__libc_csu_init+94>:       pop    r13
   0x4013d0 <__libc_csu_init+96>:       pop    r14
   0x4013d2 <__libc_csu_init+98>:       pop    r15
   0x4013d4 <__libc_csu_init+100>:      ret    
```

```bash
   0x40119c <__do_global_dtors_aux+28>: add    DWORD PTR [rbp-0x3d],ebx
   0x40119f <__do_global_dtors_aux+31>: nop
   0x4011a0 <__do_global_dtors_aux+32>: ret
```

VD: Với 2 gadget này ta có thể add vào địa chỉ chứ tại [rbp - 0x3d] với ebx ta kiểm soát.
Đồng thời ta thấy rằng binary ở đây có Partial Relro, nên ta sẽ relative add lên got table biến printf thành one_gadget.

-------------------------------------------------------------------

### Reference Source:

[+] https://ir0nstone.gitbook.io/notes/types/stack/ret2csu

[+] https://i.blackhat.com/briefings/asia/2018/asia-18-Marco-return-to-csu-a-new-method-to-bypass-the-64-bit-Linux-ASLR-wp.pdf

[+] https://gist.github.com/kaftejiman/a853ccb659fc3633aa1e61a9e26266e9
