# Format String

```python
pl += f"%{wr}c%17$hn\x00".encode()
```

- `Overview`:
    * [format-specifiers-in-c](https://www.tutorialspoint.com/format-specifiers-in-c) .

- `Technique note`:
    * Một số bài format strings cần tạo vòng lặp loop thì có rất nhiều ý tưởng để tạo vòng lặp loop: 
         + `1:` ghi đè GOT func libc đằng sau vị trí có fmt.
         + `2:` ghi đè .fini_array (Sử dụng exit(0) trực tiếp, hãy cân nhắc sử dụng fini_array và khi exit được thực thi, tất cả các hàm trong mảng .fini sẽ được duyệt và thực thi. ), ...
           ```c
           main:		%rdi
	        argc:		%rsi
	        argv:		%rdx
	        init:		%rcx
	        fini:		%r8
	        rtld_fini:	%r9
	        stack_end:	stack.	*/
           ```
         + ...
    * Blind Format String:
        + [Blind Format String video](https://www.youtube.com/watch?v=XuzuFUGuQv0) .
        + [Blind src](https://github.com/beerpwn/ctf/tree/master/2019/redpwn_ctf/black_echo) .
    * Trigger malloc or free use printf, scanf, ...
        + [VD-CTF: redpwnctf](https://scavengersecurity.com/posts/redpwnctf-simultaneity/) .
        + [VD-CTF: EasiestPrintf](https://poning.me/2017/03/23/EasiestPrintf/#:~:text=Leak%20the%20libc%20address%20from%20the%20arbitrary%20read.,the%20input.%20The%20full%20script%20is%20as%20follows) .

    * Leak flag in stack (Format String) convert:

    ```python
    >>> from pwn import *
    >>> f = b''
    >>> a = '0x....0x....0x....0x....'
    >>> a = a.split('0x')
    >>> for i in range(1, len(a)):
    >>>   f += p64(int(a[i], 16))
    >>> f = ctf{.....}
    ```
    * `Trick: `
       + Use `"*"` to have a variable field width, equals to an signed integer on the stack, can combine with positional argument. Eg. %*10$c: print a number of characters equals to the 10th argument. `[FMT XMaster - TTV KCSC 2023]`
       + Enter `.` to `scanf()` with number format `(%d, %u, %ld...)` won't enter new value to var.
       + `%*` works as `%d` and will print first 4 bytes.
       + `%.*<k>$c` will be the pad of `0` with the size that `%<k>$c` point to.
       + Format string can be use to modify and read data at the same time just in case you don't use the short format (%<k>$c), use the plain format instead (%p, %n, %s, %c).
       ```bash
       Example: %c%c%c%c%1234c%hn%6$s to change address and read from that changed address.
       ```
