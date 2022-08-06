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


>Tôi học được nó khi mà muốn cố gắng setup giá trị thanh ghi rdx để sử dụng `write` cho việc leak giá trị của `linkmap` phục vụ cho khai thác `ret2dlresolve` trên kiến trúc 64bit.

-------------------------------------------------------------------

### Reference Source:

[+] https://ir0nstone.gitbook.io/notes/types/stack/ret2csu

[+] https://i.blackhat.com/briefings/asia/2018/asia-18-Marco-return-to-csu-a-new-method-to-bypass-the-64-bit-Linux-ASLR-wp.pdf

[+] https://gist.github.com/kaftejiman/a853ccb659fc3633aa1e61a9e26266e9
