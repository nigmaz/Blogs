# FILE STRUCTURE ORIENTED PROGRAMMING

- https://github.com/nigmaz/Blogs/tree/main/Virtual-Machine/Ubuntu/Advanced/FSOP

## [0] Overview
- Filestruct allocated in heap `(VD: stream = fopen("/dev/urandom", "r");)`
- puts() calls _IO_new_file_xsputn (FILE *f, const void *data, size_t n)

## [1] Technique Attack
- FSOP có hai kiểu attack 1 là corrupt file stream của libc (thường là stdout để leak), hai là fake hoặc corrupt file stream của chương trình khởi tạo (có thể là vtable, cả struct file, ...) và một dạng nữa là kết hợp cùng tấn công HEAP.
- FSOP technique
   *  `_IO_FILE-Arbitrary-Address-Read` | stdout => read arbitrary 
   *  `_IO_FILE-Arbitrary-Address-Write` |stdin => write arbitrary
   *  `iofile_aw`
   *  `Bypass-IO_validate_vtable`
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
    * Tự giải bài ở BKCTF
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
- _IO_FILE : Cấu trúc biểu diễn luồng tệp trong thư viện chuẩn của hệ thống Linux.

- Bảng hàm ảo (vtable) : Là bảng được cấp phát khi định nghĩa lớp và sử dụng hàm ảo trong ngôn ngữ lập trình hướng đối tượng
```c
struct _IO_FILE_plus
{
  FILE file;
  const struct _IO_jump_t *vtable;
};
struct _IO_FILE
{
  int _flags;		/* High-order word is _IO_MAGIC; rest is flags. */
  /* The following pointers correspond to the C++ streambuf protocol. */
  char *_IO_read_ptr;	/* Current read pointer */
  char *_IO_read_end;	/* End of get area. */
  char *_IO_read_base;	/* Start of putback+get area. */
  char *_IO_write_base;	/* Start of put area. */
  char *_IO_write_ptr;	/* Current put pointer. */
  char *_IO_write_end;	/* End of put area. */
  char *_IO_buf_base;	/* Start of reserve area. */
  char *_IO_buf_end;	/* End of reserve area. */
  /* The following fields are used to support backing up and undo. */
  char *_IO_save_base; /* Pointer to start of non-current get area. */
  char *_IO_backup_base;  /* Pointer to first valid character of backup area */
  char *_IO_save_end; /* Pointer to end of non-current get area. */
  struct _IO_marker *_markers;
  struct _IO_FILE *_chain;
  int _fileno;
  int _flags2;
  __off_t _old_offset; /* This used to be _offset but it's too small.  */
  /* 1+column number of pbase(); 0 is unknown. */
  unsigned short _cur_column;
  signed char _vtable_offset;
  char _shortbuf[1];
  _IO_lock_t *_lock;
#ifdef _IO_USE_OLD_IO_FILE
};
```
```c
struct _IO_jump_t
{
    JUMP_FIELD(size_t, __dummy);
    JUMP_FIELD(size_t, __dummy2);
    JUMP_FIELD(_IO_finish_t, __finish);
    JUMP_FIELD(_IO_overflow_t, __overflow);
    JUMP_FIELD(_IO_underflow_t, __underflow);
    JUMP_FIELD(_IO_underflow_t, __uflow);
    JUMP_FIELD(_IO_pbackfail_t, __pbackfail);
    /* showmany */
    JUMP_FIELD(_IO_xsputn_t, __xsputn);
    JUMP_FIELD(_IO_xsgetn_t, __xsgetn);
    JUMP_FIELD(_IO_seekoff_t, __seekoff);
    JUMP_FIELD(_IO_seekpos_t, __seekpos);
    JUMP_FIELD(_IO_setbuf_t, __setbuf);
    JUMP_FIELD(_IO_sync_t, __sync);
    JUMP_FIELD(_IO_doallocate_t, __doallocate);
    JUMP_FIELD(_IO_read_t, __read);
    JUMP_FIELD(_IO_write_t, __write);
    JUMP_FIELD(_IO_seek_t, __seek);
    JUMP_FIELD(_IO_close_t, __close);
    JUMP_FIELD(_IO_stat_t, __stat);
    JUMP_FIELD(_IO_showmanyc_t, __showmanyc);
    JUMP_FIELD(_IO_imbue_t, __imbue);
};

gdb-peda$ p *(struct _IO_jump_t *)0x00007ffff7dca2a0
$32 = {
  __dummy = 0x0, 
  __dummy2 = 0x0, 
  __finish = 0x7ffff7a6e400 <_IO_new_file_finish>, 
  __overflow = 0x7ffff7a6f3d0 <_IO_new_file_overflow>, 
  __underflow = 0x7ffff7a6f0f0 <_IO_new_file_underflow>, 
  __uflow = 0x7ffff7a70490 <__GI__IO_default_uflow>, 
  __pbackfail = 0x7ffff7a71d20 <__GI__IO_default_pbackfail>, 
  __xsputn = 0x7ffff7a6da00 <_IO_new_file_xsputn>, 
  __xsgetn = 0x7ffff7a6d660 <__GI__IO_file_xsgetn>, 
  __seekoff = 0x7ffff7a6cc60 <_IO_new_file_seekoff>, 
  __seekpos = 0x7ffff7a70a60 <_IO_default_seekpos>, 
  __setbuf = 0x7ffff7a6c920 <_IO_new_file_setbuf>, 
  __sync = 0x7ffff7a6c7a0 <_IO_new_file_sync>, 
  __doallocate = 0x7ffff7a601e0 <__GI__IO_file_doallocate>, 
  __read = 0x7ffff7a6d9e0 <__GI__IO_file_read>, 
  __write = 0x7ffff7a6d260 <_IO_new_file_write>, 
  __seek = 0x7ffff7a6c9e0 <__GI__IO_file_seek>, 
  __close = 0x7ffff7a6c910 <__GI__IO_file_close>, 
  __stat = 0x7ffff7a6d250 <__GI__IO_file_stat>, 
  __showmanyc = 0x7ffff7a71ea0 <_IO_default_showmanyc>, 
  __imbue = 0x7ffff7a71eb0 <_IO_default_imbue>
}
```
