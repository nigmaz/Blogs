# SROP
>Được sử dụng để kiếm soát tất cả các thanh ghi cùng một lúc.

`Sigreturn` là một loại syscall đặc biệt. Mục đích của sigreturn là quay trở lại từ `signal handler` và trả lại tất cả các giá trị thanh ghi được lưu trữ trên ngăn xếp sau khi tín hiệu đã được bỏ chặn. 

Vì vậy, bằng cách tận dụng sigreturn, nếu như chúng ta có thể làm giả cấu trúc là tập hợp các giá trị của các thanh ghi được lưu trên stack, chúng ta có thể `kiểm soát tất cả các giá trị đăng ký cùng một lúc.`

### 1) Khái niệm liên quan

Để hiểu cách thức hoạt động của SROP, ta sẽ tìm hiểu về cách mà hệ thống xử lý khi một tín hiệu xuất hiện trong hệ thống Unix.

- Chương trình sẽ tạm dừng tiến trình đang diễn ra để chuyển sang một tiến trình nhằm xử lý tín hiệu.

- Để có thể tiếp tục tiến trình được tạm dừng khi đã xử lý xong tín hiệu xuất hiện kia, ngữ cảnh của tiến trình tạm dừng được đẩy lên lưu trữ trên stack(register, flag, stack pointer, instruction pointer, ...). Ngữ cảnh có dạng cấu trúc `"sigcontext"`.

<h1 align="center"> <img height=500 src="https://github.com/l1j9m4-0n1/Blogs/blob/main/Technique/SROP/sigcontext.png"> </h1>

- Khi trình xử lý kết thúc, `sigreturn()` được gọi => giá trị trong ngữ cảnh được lưu trên stack được trả về với các thanh ghi và xóa chúng trên stack.

<h1 align="center"> <img height=200 src="https://github.com/l1j9m4-0n1/Blogs/blob/main/Technique/SROP/sigreturn.png"> </h1>

>=> Vì vậy cuộc tấn công sử dụng `SROP` hoạt động bằng cách đẩy cấu trúc `sigcontext giả mạo` lên stack, ghi đè `return address` ban đầu bằng vị trí của `gadget` cho phép thiết lập các giá trị liên quan để thực hiện syscall `sigreturn`.

### 2) Giải quyết vấn đề 

=> Cần một số yếu tố tùy thuộc vào quá trình khai thác để thực hiện `SROP` nhưng cơ bản là ba điều sau.

- Tất nhiên đầu tiên là lỗ hổng `buffer overflow`.
- Một cách để đặt giá trị thanh ghi `rax` = `0xf` (64bit) hoặc `eax` = `0x77` (32bit) 
- Gadget `syscall ; ret`

### Note:
```
rt-sigreturn | 0xf <x86_64>
sigreturn | 0x77 <x86>
```

Thiết lập giá trị cho `rax | eax` là vấn đề lớn nhất, có rất nhiều cách để làm điều đó và nó phụ thuộc vào mục tiêu mà chúng ta khai thác. Tôi sẽ trình bày trên cấu trúc 64bit(32bit chỉ khác về giá trị muốn đặt lên eax còn cách thực hiện vẫn vậy) và chỉ liệt kê các cách có thể, nếu muốn tìm hiểu rõ hơn bạn có thể đọc bài viết này [SROP](https://rog3rsm1th.github.io/posts/sigreturn-oriented-programming/).

1. mov rax, 0xf ; ret
2. pop rax ; ret
3. Sử dụng `the read` syscall để thiết lập giá trị `rax` = 0xf
4. ...

### Note:
>Ở cách thứ ba ta lợi dụng vào một tính chất thú vị của syscall `read` là ghi lại số byte được đọc vào thanh ghi `rax`. Có hai cách để lợi dụng điều đó.

- **Sử dụng gadget `mov rax, 0x0`.**

|    Padding until we reach the saved `rip`    | 
| :------------------------------------------: |
|   address of the `mov rax, 0x0; ret` gadget  |
|     address of the `syscall; ret` gadget     |

Sau đó nhập vào một chuỗi dài 15 ký tự `(0xf = 15)`, điều này sẽ cho phép chúng tôi đặt giá trị 0xf trong eax.

Và sau đó là:

|   address of the `syscall ; ret` gadget        |
| :------------------------------------------:   |
|SigContext structure with the desired parameters|

- **Sử dụng gadget `pop rax`.**

|    Padding until we reach the saved `rip`    | 
| :------------------------------------------: |
|   address of the `pop rax ; ret` gadget      |
|        `0x0` (`read` syscall number)         |
|     address of the `syscall; ret` gadget     |

Sau đó nhập vào một chuỗi dài 15 ký tự `(0xf = 15)`, điều này sẽ cho phép chúng tôi đặt giá trị 0xf trong eax.

Và sau đó là:

|   address of the `syscall ; ret` gadget        |
| :------------------------------------------:   |
|SigContext structure with the desired parameters|

>Note: Ở trường hợp thứ hai này bạn có thể tận dụng trực tiếp gadget `pop rax ; ret`.

### 3) Ví dụ về tùy chỉnh `Sigcontext`

Khi đã tìm ra cách gọi `syscall sigreturn`, chúng ta cần tìm cách lấy shell thông qua `Sigcontext` sẽ được khôi phục từ stack. `Pwntools` hỗ trợ rất mạnh trong việc setup trực tiếp giá trị của thanh ghi mà ta muốn thay vì phải viết lại nguyên một `Sigcontext` và mất thời gian thiết lập các giá trị không lien quan đến mục tiêu. 

1. **Nếu file có sẵn chuỗi `/bin/sh`**.

Ý tưởng là gọi hàm `execve` `(syscall 0x3b -> 59 ở dạng thập phân)` với chuỗi `/bin/sh` là tham số sẽ lấy được `shell`. Chuỗi `/bin/sh` có thể có sẵn trong file hoặc chúng ta có thể ghi nó vào vùng nhớ mà biết rõ địa chỉ.

| `Register` | `Value`           |
|:----------:|:-----------------:|
| `rip`      |`syscall` instruction address|
| `rax`      |`0x3b` (`execve` syscall)|
| `rdi`      |address of `/bin/sh`|
| `rsi`      |0x0 (`NULL`)|
| `rdi`      |0x0 (`NULL`)|

2. **Sử dụng `mprotect`**.

>`mprotect`: set protection on a region of memory

Sử dụng `mprotect` để làm cho một vùng bộ nhớ mà chúng tôi lựa chọn có thể thực thi và có thể ghi được để cho phép thực thi `shellcode` tại địa chỉ đó. Sau đó, chúng tôi chuyển stack đến khu vực đó để chúng tôi có thể dễ dàng ghi dữ liệu vào nó. Chúng tôi đưa vào địa chỉ `rsp` chứa điểm vào của chương trình để đảm bảo tiến trình điều khiển diễn ra bình thường. Sau đó, chúng tôi có thể sắp xếp chuyển hướng chương trình đến địa chỉ `shellcode`, địa chỉ này sẽ được thực thi bất chấp `the NX protection`.

| `Register` | `Value`           |
|:----------:|:-----------------:|
| `rax`      |`0xa` (`mprotect` syscall)|
| `rdi`      |address shellcode|
| `rsi`      |size (`0x1000` for exemple)|
| `rdx`      |`0x7` -> mode (rwx)|
| `rsp`      |entrypoint (new stack)|
| `rip`      |address of the `syscall; ret` gadget|

### 4) Practice example

[1] [miniPwn](https://hackmd.io/@imth/SROP)

[2] [BUUCTF](https://www.cnblogs.com/xlrp/p/14273599.html)

---------------------------------------------------

### Reference Source:

[+] https://rog3rsm1th.github.io/posts/sigreturn-oriented-programming/

[+] https://ir0nstone.gitbook.io/notes/types/stack/syscalls/sigreturn-oriented-programming-srop

[+] https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6956568

[+] https://bananamafia.dev/post/srop/
