# Attack vtable

## [0] Overview

- Nếu kiểm tra liên tục các macro được định nghĩa, cuối cùng sẽ thấy nó tham chiếu đến biến vtable. Tất cả các chức năng tệp, bao gồm fread sẽ cố gắng hoạt động trên các tệp bằng cách tham chiếu vtable. Tuy nhiên vì vtable là một khu vực được allocate dynamic (heap segment has rw_) nên nó có thể bị khai thác tấn công.
    * Ví dụ: khi fclose(FILE *ptr) được gọi, con trỏ hàm được lưu trữ trong trường __finish trong cấu trúc sẽ được gọi sau khi giải phóng các cấu trúc bên trong.

- Tất cả các file đều dùng chung 1 vtable, kiến trúc 64 bit nằm ở offset `0xd8` .

## [1] Technique Attack

- Kỹ thuật này thay đổi theo 3 mốc versions của g-libc 2.23, 2.27, 2.29,...

- `Glibc-2.23` chỉ cần fake struct *vtable mà không cần để ý đến các hàm security check.
    * VD: `seethefile-pwnable.tw`,...

- `Glibc-2.27` => `Bypass IO_validate_vtable()` > Hàm kiểm tra xem địa chỉ hàm của vtable được tham chiếu bởi hàm tệp có tồn tại trong phần __libc_IO_vtables hay không.
    * Pointer *vtables được gán cho phần __libc_IO_vtables. Mã trừ địa chỉ bắt đầu và kết thúc của section để tìm ra kích thước của section và nếu địa chỉ của vtable được gọi nằm ngoài kích thước của section, hàm _IO_vtable_check sẽ được gọi để tạo ra lỗi.
    * Bypass thông qua IO_str_overflow: https://dhavalkapil.com/blogs/FILE-Structure-Exploitation/
    * VD: https://learn.dreamhack.io/272

- `Glibc-2.29` Trong thư viện glibc 2.29 trở lên, mã gọi con trỏ hàm bên trong hàm IO_str_overflow đã bị xóa nên các kỹ thuật tấn công sử dụng hàm đó không thể sử dụng được nữa.
    * https://blog.kylebot.net/2022/10/22/angry-FSROP/

 
