# SROP
>Được sử dụng để kiếm soát tất cả các thanh ghi cùng một lúc.

Sigreturn là một loại syscall đặc biệt. Mục đích của sigreturn là quay trở lại từ `signal handler` và trả lại tất cả các giá trị thanh ghi được lưu trữ trên ngăn xếp sau khi tín hiệu đã được bỏ chặn. 

Vì vậy, bằng cách tận dụng sigreturn, nếu như chúng ta có thể làm giả cấu trúc là tập hợp các giá trị của các thanh ghi được lưu trên stack, chúng ta có thể kiểm soát tất cả các giá trị đăng ký cùng một lúc.

### 1) Một số khái niệm liên quan

Để hiểu cách thức hoạt động của SROP, ta sẽ tìm hiểu về cách mà hệ thống xử lý khi một tín hiệu xuất hiện trong hệ thống Unix.

- Chương trình sẽ tạm dừng tiến trình đang diễn ra để chuyển sang một tiến trình nhằm xử lý tín hiệu.

- Để có thể tiếp tục tiến trình được tạm dừng khi đã xử lý xong tín hiệu xuất hiện kia, ngữ cảnh của tiến trình tạm dừng được đẩy lên lưu trữ trên stack(register, flag, stack pointer, instruction pointer, ...). Ngữ cảnh có dạng cấu trúc "sigcontext".

<h1 align="center"> <img height=500 src="https://github.com/l1j9m4-0n1/Blogs/blob/main/Technique/SROP/sigcontext.png"> </h1>

- Khi trình xử lý kết thúc, `sigreturn()` được gọi => giá trị trong ngữ cảnh được lưu trên stack được trả về với các thanh ghi và xóa chúng trên stack.

<h1 align="center"> <img height=250 src="https://github.com/l1j9m4-0n1/Blogs/blob/main/Technique/SROP/sigreturn.png"> </h1>

---------------------------------------------------

### Reference Source:

[+] 

[+] 

[+]
