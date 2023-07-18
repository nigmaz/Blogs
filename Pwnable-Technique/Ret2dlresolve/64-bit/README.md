# 64-bit

- Trường hợp [lazenca](https://www.lazenca.net/pages/viewpage.action?pageId=19300744) là VD leak `link_map` để ghi đè `link_map + 0x1d0` (hoặc + 0x1c8), trong VD tôi biên dịch .bss vẫn được ánh xạ tại vùng nhớ 0x40xxxx nhưng tôi vẫn viết payload ghi đè `link_map` để có VD về việc khai thác khi .bss ánh xạ tại 0x60xxxx.

- Trường hợp [syst3mfailure](https://syst3mfailure.io/ret2dl_resolve) là VD không cần leak `link_map`.

>Trong trường hợp cần leak thì khi có hàm `write` từ libc bạn cũng có thể lựa chọn khai thác `ret2libc` nên chọn kỹ thuật khai thác nào phụ thuộc vào bạn và ngữ cảnh bạn đang khai thác(có thể khi không cung cấp libc thì khó tìm chính xác offset thì sẽ dùng ret2dlresolve hoặc là dùng DynELF).

- __[NOTE]__:

    * `1)` Trong x64 thì giá trị Rel_offset là chỉ số mảng của struct Elf64_Rela so với JMPREL, không phải là offset của địa chỉ entry so với JMPREL.

    * `2)` Struct JUMREL have idx start 0; Struct SYMTAB have idx start 0 but value is store start idx = 1.

- link_map các version có sự khác biệt về nơi cần ghi đè để tránh báo lỗi:
    * link_map+0x1c8

    * link_map+0x1d0

- Thông thường, khi thực hiện ret2dlresolve trên 64-bit, mình sẽ kiểm tra xem địa chỉ có ghi được thuộc khoảng nào. Nếu thuộc vào khoảng 0x40xxxx thì ta chắc chắn 
thực hiện được ret2dlresolve. Nhưng nếu địa chỉ là 0x60xxxx thì sẽ bị lỗi ngay tại lúc kiểm tra version của dlresolver.



