# FILE STRUCTURE ORIENTED PROGRAMMING

- Setup debug internal function g-libc:
    * https://github.com/nigmaz/Blogs/tree/main/Virtual-Machine/Ubuntu#612-fsop---add-libc-source-code-to-gdb

## [0] Overview

- `The File Struct` allocated in heap `(VD: stream = fopen("/dev/urandom", "r");)` except stdin, stdout, stderr.
- Các bước OPEN FILE:
   * 1. Malloc FILE structure
   * 2. Gán vtable vào FILE structure
   * 3. Khởi tạo FILE structure
   * 4. Liên kết FILE structure vào _IO_list_all
   * 5. Call system khởi tạo file.
- Các bước CLOSE FILE:
   * 1. Unlink FILE structure ra khỏi _IO_list_all
   * 2. Call system đóng file.
   * 3. _IO_FINISH trong vtable được thực thi.
- `References:`
    * https://nightrainy.github.io/2019/08/07/play-withe-file-structure-%E6%90%AC%E8%BF%90/
    * https://sh4dy.com/notes/pwn/heap-exploitation/fsop.html
    * https://chovid99.github.io/posts/file-structure-attack-part-1/

## [1] Technique Attack
- FSOP có hai kiểu attack 
  * `1.` là corrupt file stream của libc (thường là stdout để leak hoặc ít hơn là stdin để đọc tùy ý). 
  * `2.` là fake hoặc corrupt file stream của chương trình khởi tạo (có thể là vtable, cả struct file, ...) 
  * `3.` một dạng nữa là kết hợp cùng tấn công HEAP (House of Orange) hoặc các dạng tấn công khác.
- FSOP technique
   *  `_IO_FILE-Arbitrary-Address-Read`  | stdout => read arbitrary 
   *  `_IO_FILE-Arbitrary-Address-Write` |stdin => write arbitrary
   *  `*vtable attack`
   * ...
- `GDB Script`
    ```bash
    gdb> p *stdin
    gdb> p *stdout
    gdb> p *stderr
    ```

    * [_IO_FILE_plus](https://elixir.bootlin.com/glibc/glibc-2.23/source/libio/libioP.h#L342)
    ```c
    gdb> p *(struct _IO_FILE_plus *)<Address struct _IO_FILE_plus>
    ...
    struct _IO_FILE_plus
    {
      FILE file;
      const struct _IO_jump_t *vtable;
    };
    ```
    * [_IO_FILE](https://elixir.bootlin.com/glibc/glibc-2.23/source/libio/libio.h#L241)
    ```c
    gdb> p *(struct _IO_FILE *)<Address struct _IO_FILE>
    ...
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
    * [_IO_jump_t](https://elixir.bootlin.com/glibc/glibc-2.23/source/libio/libioP.h#L307)    
    ```c
    gdb> p *(struct _IO_jump_t *)<Address *vtable>
    ...
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
    ```
## [2] References CTF
- ...





