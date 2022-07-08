# Stack Pivot

>Sử dụng nếu thiếu không gian ghi đè sau `Return address` trên Stack khi thực hiện ROP hoặc thiết lập giá trị đối số cho hàm.

Khi thực hiện `Stack Pivot`, cần tìm gadget giúp kiểm soát được giá trị lưu trong thanh ghi `RSP` và giả mạo vị trí của Stack. Có một số cách để làm điều này. 

### 1) pop rsp

Đẩy trực tiếp giá trị trên stack do ta kiểm soát ra thanh ghi rsp. Nhưng rất ít khi xảy ra trường hợp này. 

### 2) xchg <register>, rsp

```asm
pop <register>                <=== return pointer
<register value>
xchg <register>, rsp
```

Ta có thể sử dụng một thanh ghi trung gian tùy vào gadget để lưu giá trị mà ta muốn lưu trên rsp, sau đó instruction `xchg` sẽ đổi giá trị thanh ghi rsp với thanh ghi trung gian. Trường hợp này cũng ít được sử dụng tới.

### 3) leave ; ret

Đây là trường hợp tôi thấy được sử dụng nhiều nhất. Mọi hàm con của chương trình (trừ main) đều kết thúc bằng `leave ; ret`. Cụ thể gadget `leave ; ret` thực hiện quá trình sau.

```asm
mov rsp, rbp
pop rbp
pop rip
```

Điều này có nghĩa là với `leave ; ret` của function ta có thể kiểm soát được giá trị trên `rbp` sau đó ta ghi đè `return address` bằng địa chỉ của gadget `leave ; ret` (nghĩa là ta đang thực hiện leave ; ret hai lần). Sau đó `mov rsp, rbp` sẽ chuyển giá trị trong `rbp` lên `rsp` khi đó ta dễ dàng kiểm soát được giá trị trên rsp.

### Note: Sử dụng cả trên 32bit và 64bit.

----------------------------------------------------------------------------

### Reference Source:

[+] https://ir0nstone.gitbook.io/notes/types/stack/stack-pivoting
