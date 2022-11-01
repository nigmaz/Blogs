# NOTE

>`lazenca` là VD leak `link_map` để ghi đè `link_map + 0x1d0` (hoặc + 0x1c8), trong VD tôi biên dịch .bss vẫn được ánh xạ tại vùng nhớ 0x40xxxx nhưng tôi vẫn viết payload ghi đè để có VD về việc khai thác khi .bss ánh xạ tại 0x60xxxx.

>`syst3mfailure` là VD không cần leak `link_map`.

 - Trong trường hợp cần leak thì khi có hàm `write` từ libc bạn cũng có thể lựa chọn khai thác `ret2libc` nên chọn kỹ thuật khai thác nào phụ thuộc vào bạn và ngữ cảnh bạn đang khai thác.

[NOTE]:

1) Do đó, giá trị Reset_offset phải là chỉ số mảng của cấu trúc Elf64_Rela, không phải là giá trị bù đắp của địa chỉ.

2) Struct JUMREL have idx start 0; Struct SYMTAB have idx start 0 but value is store start idx = 1.

Thông thường, khi mình thực hiện ret2dlresolve trên 64 bit, mình sẽ kiểm tra xem địa chỉ có ghi được thuộc khoảng nào. Nếu thuộc vào khoảng 0x40xxxx thì ta chắc chắn 
thực hiện được ret2dlresolve. Nhưng nếu địa chỉ là 0x60xxxx thì sẽ bị lỗi ngay tại lúc kiểm tra version của dlresolver.

link_map+0x1c8

link_map+0x1d0

 - VD Source: [lazenca]( https://www.lazenca.net/pages/viewpage.action?pageId=19300744) .
 
 - VD Source: [syst3mfailure](https://syst3mfailure.io/ret2dl_resolve) .

