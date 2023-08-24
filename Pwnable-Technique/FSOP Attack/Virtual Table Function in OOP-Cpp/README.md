# Virtual Table Function in OOP-Cpp
- Vtable and Vpointer
    * https://viblo.asia/p/co-che-virtual-table-yMnKMMLAK7P
    * https://cppdeveloper.com/c-nang-cao/virtual-tables-vtable-trong-c/
- Virtual Method
    * https://cppdeveloper.com/c-co-ban/6-3-1-ghi-de-phuong-thuc-trong-lop-dan-xuat-1/
      
- `VirtualTable` contain ptr* `VirtualFunction`.

- Pointer `_vptr` created when (class define this object declare `virtual function` - Khai báo `virtual class`)

- Khi một đối tượng được tạo ra với khai báo `virtual function` thì đồng thời _vptr cũng được tạo ra để trỏ đến virtual table của đối tượng đó. VD: 
Đối tượng b được tạo ra, thì con trỏ _vptr cũng được khai báo để trỏ tới virtual table của đối tượng b
