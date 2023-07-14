# Format String

- Overview:
    * [format-specifiers-in-c](https://www.tutorialspoint.com/format-specifiers-in-c) .


- Technique note:
    * Một số bài format strings cần tạo vòng lặp loop thì có rất nhiều ý tưởng để tạo vòng lặp loop: 
         + `1:` ghi đè GOT func libc đằng sau vị trí có fmt.
         + `2:` ghi đè .fini_array, ...
         + ...
    * Use `"*"` to have a variable field width, equals to an signed integer on the stack, can combine with positional argument. Eg. %*10$c: print a number of characters equals to the 10th argument. `[FMT XMaster - TTV KCSC 2023]`
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