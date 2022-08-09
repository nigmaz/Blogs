# NOTE

>`syst3mfailure` là VD không cần leak `link_map`.

>`lazenca` là VD leak `link_map` để ghi đè `link_map + 0x1d0` (hoặc + 0x1c8), trong VD tôi biên dịch .bss vẫn được ánh xạ tại vùng nhớ 0x40xxx nhưng tôi vẫn viết payload ghi đè để có VD về việc khai thác khi .bss ánh xạ tại 0x60xxxx.

Trong trường hợp cần leak thì khi có hàm `write` từ libc bạn cũng có thể lựa chọn khai thác `ret2libc` nên chọn kỹ thuật khai thác nào phụ thuộc vào bạn và ngữ cảnh bạn đang khai thác.


