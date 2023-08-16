# Exploit Bypass Seccomp

- https://dreamhack.io/?obj=221
- [KMACTF2022 - Duet](https://github.com/nhtri2003gmail/CTFWriteup/tree/master/2022/KMACTF-2022/Duet)
- [https://github.com/david942j/seccomp-tools](https://github.com/david942j/seccomp-tools)
- [https://pypi.org/project/pwnsandbox/](https://pypi.org/project/pwnsandbox/)

## +) seccomp-tools (Tools for seccomp)

```bash
$ sudo apt install -y gcc ruby-dev && \
sudo gem install seccomp-tools
```


```bash
Để thực hiện SYSCALL READ, trước tiên chúng ta cần mở tệp. 
Thật không may, chúng tôi không cho phép thực hiện OPEN SYSCALL. 
Tuy nhiên, đây là một mẹo nhỏ: như chúng ta đã biết, 
chúng ta có thể thực thi một syscall với lệnh syscall (dành cho 64 bit) 
hoặc int 0x80 (dành cho 32 bit). 
Vì 64 bit lớn hơn 32 bit nên chúng ta có thể thực thi 
int 0x80 trên 64 bit với tất cả các đối số tương tự như những gì chúng ta thực hiện trên 32 bit. 

Nói cách khác, nếu chúng ta muốn thực thi int 0x80, 
chúng ta cần đặt rax, rbx, rcx và rdx nhưng nó chỉ lấy 32 bit đầu tiên của các thanh ghi, 
đó là eax, ebx, ecx và edx.

Vì vậy, đối với con trỏ tên tệp, chúng tôi sẽ cần nó tối đa là 32 bit. 
Và địa chỉ lý tưởng là địa chỉ chúng tôi đã thay đổi quyền thành rwx 
vì nó chỉ chiếm 3 byte. 
Vì vậy, hãy di chuyển đường dẫn của cờ đến địa chỉ đó bằng tập lệnh này.

Vì vậy, thanh ghi rbp chứa đường dẫn chính xác của cờ. 
Bây giờ chúng tôi sẽ muốn thực thi int 0x80 để mở tệp. 
Mặc dù chúng tôi không cho phép SYSCALL OPEN trên 64 bit, 
nhưng đó chỉ là vấn đề nếu chúng tôi sử dụng SYSCALL OPEN (cho 64 bit) 
vì giá trị rax của open khi chúng tôi sử dụng SYSCALL OPEN là 2 không được phép:

But if we execute syscall open with int 0x80 (for 32 bit), the rax value will be 5

And rax value of 5 is allowed because in seccomp (base on 64 bit), 
the value of rax is 5 is SYSCALL FSTAT which is allowed in seccomp.
```
