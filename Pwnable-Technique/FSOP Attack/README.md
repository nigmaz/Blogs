![image](https://github.com/nigmaz/Blogs/assets/75942822/cf22b663-261a-4595-aa34-32b89c513cb5)![image](https://github.com/nigmaz/Blogs/assets/75942822/9da4e8e4-faf2-4c16-923a-30153c423d85)# FILE STRUCTURE ORIENTED PROGRAMMING

## [0] Overview
- Filestruct allocated in heap `(VD: stream = fopen("/dev/urandom", "r");)`
- puts() calls _IO_new_file_xsputn (FILE *f, const void *data, size_t n)

## [1] Technique Attack
- FSOP có hai kiểu attack 1 là corrupt file stream của libc (thường là stdout để leak), hai là fake hoặc corrupt file stream của chương trình khởi tạo (có thể là vtable, cả struct file, ...) và một dạng nữa là kết hợp cùng tấn công HEAP.
- FSOP technique
   *  _IO_FILE-Arbitrary-Address-Read | stdout => read arbitrary 
   *  _IO_FILE-Arbitrary-Address-Write |stdin => write arbitrary
   *  iofile_aw
   *  Bypass-IO_validate_vtable
   * ...
- Attack FSOP + Heap
   * Use null byte overflow to get overlapping chunks. Allocate chunk in stdout->flags and partial overwrite IO_write_base to get leak. Then allocation at __free_hook and overwrite with one_gadget.


## [2] References
- Overview:
    * [FSOP angelboy](https://nightrainy.github.io/2019/08/07/play-withe-file-structure-%E6%90%AC%E8%BF%90/?fbclid=IwAR06PLkixggoSadl1ANGvZNW4zgfNOgcs5VC2l2IHtFzEVclUJzFp2NObsI#content) .
    * [Dreamhack slide](https://learn.dreamhack.io/271#4) .
    * [Tổng hợp tiếng việt](https://hackmd.io/@ductin/r1b8nhBs5) .
- Technique:
    * [Dreamhack _IO_FILE Arbitrary Address Read](https://wyv3rn.tistory.com/111) .
    * [bypass vtable check](https://dhavalkapil.com/blogs/FILE-Structure-Exploitation/) .
    * https://outflux.net/blog/archives/2011/12/22/abusing-the-file-structure/
    * MICS technique with HEAP ATTACK:
        + House of orange
    * https://blog.kylebot.net/2022/10/22/angry-FSROP/
    * [FSOP + HEAP](https://ret2school.github.io/post/mailman/) .
- `GDB Script`
```bash
gdb> p *stdout
gdb> ptype FILE
gdb> dt FILE
gdb> p/x _IO_2_1_stdout_
gdb> x/28gx &_IO_2_1_stdout_
gdb> x/100gx &_IO_file_jumps

gef➤  print _IO_list_all
$23 = (struct _IO_FILE_plus *) 0x7ffff7dd2520 <_IO_2_1_stderr_>
gef➤  print _IO_2_1_stderr_.file._chain
$24 = (struct _IO_FILE *) 0x7ffff7dd2600 <_IO_2_1_stdout_>
gef➤  print _IO_2_1_stdout_.file._chain
$25 = (struct _IO_FILE *) 0x7ffff7dd18c0 <_IO_2_1_stdin_>
gef➤  print _IO_2_1_stdin_.file._chain
$26 = (struct _IO_FILE *) 0x0
```
