# _IO_FILE-Arbitrary-Address-Write


```c
Arbitrary_Address_Write | fread, fgets
read(f->_fileno, _IO_buf_base, _IO_buf_end - _IO_buf_base);
f-> fileno = stdin
_IO_buf_base = địa chỉ muốn ghi
_IO_buf_end = địa chỉ muốn ghi + 1024
```

- `Lưu ý:`
    * Lý do thêm một số lớn hơn 1024 là vì có một điều kiện trong mã `_IO_new_file_underflow` rằng giá trị của `_IO_buf_end - _IO_buf_base` phải lớn hơn kích thước đọc được truyền dưới dạng đối số cho hàm fread. Nếu điều kiện đó được đáp ứng, bạn có thể chỉ cần ghi đè fileno , tức là bộ mô tả tệp bằng 0 đại diện cho stdin.
    * `1-Sửa fd khác => stdout => leak` và `2-Sửa chính stdout để leak` .
