# _rtld_global

- Struct `_rtld_global` nằm trong ld.so (rw_).
- exit() => _fini_array => _dl_fini
- Hàm `_dl_fini` (khác _init_array) gọi hàm `__rtld_lock_lock_recursive` với `_ld_load_lock` làm đối số. Hàm và các đối số của nó là thành viên của struct `_rtld_global` và khu vực này có quyền ghi.
- Ta có thể thực thi `system("/bin/sh\x00")` nếu:
    * Pointer `__rtld_lock_lock_recursive` = `system()` .
    * Giá trị của `_ld_load_lock` trỏ đến chuỗi `"/bin/sh\x00"` .
