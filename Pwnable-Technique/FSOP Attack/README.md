# FILE STRUCTURE ORIENTED PROGRAMMING

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
- gdb:

```bash
ptype FILE
dt FILE
 => view FILE STRUCT 
 
 p/x _IO_2_1_stdout_
x/28gx &_IO_2_1_stdout_

Use null byte overflow to get overlapping chunks. Allocate chunk in stdout->flags and partial overwrite IO_write_base to get leak. Then allocation at __free_hook and overwrite with one_gadget.


puts() calls _IO_new_file_xsputn (FILE *f, const void *data, size_t n)

gef➤  print _IO_list_all
$23 = (struct _IO_FILE_plus *) 0x7ffff7dd2520 <_IO_2_1_stderr_>
gef➤  print _IO_2_1_stderr_.file._chain
$24 = (struct _IO_FILE *) 0x7ffff7dd2600 <_IO_2_1_stdout_>
gef➤  print _IO_2_1_stdout_.file._chain
$25 = (struct _IO_FILE *) 0x7ffff7dd18c0 <_IO_2_1_stdin_>
gef➤  print _IO_2_1_stdin_.file._chain
$26 = (struct _IO_FILE *) 0x0

x/100gx &_IO_file_jumps
```
