# _IO_FILE-Arbitrary-Address-Read

- Quá trình đọc và ghi file sử dụng con trỏ và giá trị của struct _IO_FILE bên trong library.
- Abitrary read = cách thao tác với struct _IO_FILE trong quá trình ghi writefile sử dụng `fwrite, fputs`

```c
write(f->_fileno, _IO_write_base, _IO_write_ptr - _IO_write_base);
f-> fileno = stdout
_IO_write_base = flag_buf
_IO_write_ptr = flag_buf + 1024
```

- `Lưu ý: `
    * Bạn có thể thấy rằng việc khai thác thao túng con trỏ _IO_read_end đến địa chỉ của flag_buf, địa chỉ này không cần thiết cho đầu ra. Điều này là để tránh gọi lệnh gọi hệ thống lseek bên trong hàm new_do_write.

    * To achieve arbitrary reading, we can set _IO_read_ptr and _IO_read_base to target_address and _IO_read_end to target_address + 400

    * Other than that, all the entries can be set to NULL except for _lock and _flags.
