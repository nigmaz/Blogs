section    .text
global    _start

_start:
    push _write
    mov rdi,0
    mov rsi,rsp
    sub rsi,8
    mov rdx,300
    mov rax,0
    syscall
    ret

_write:
    push _exit
    mov rsi,rsp
    sub rsi,8
    mov rdx,8
    mov rax,1
    mov rdi,1
    syscall
    ret

_exit:
    mov rax,0x3c
    syscall


--------------------------------------------------
   0x401000 <_start>:		push   0x40101e
   0x401005 <_start+5>:		mov    edi,0x0
   0x40100a <_start+10>:	mov    rsi,rsp
   0x40100d <_start+13>:	sub    rsi,0x8
   0x401011 <_start+17>:	mov    edx,0x12c
   0x401016 <_start+22>:	mov    eax,0x0
   0x40101b <_start+27>:	syscall 
   0x40101d <_start+29>:	ret
       
   0x40101e <_write>:		push   0x40103c
   0x401023 <_write+5>:		mov    rsi,rsp
   0x401026 <_write+8>:		sub    rsi,0x8
   0x40102a <_write+12>:	mov    edx,0x8
   0x40102f <_write+17>:	mov    eax,0x1
   0x401034 <_write+22>:	mov    edi,0x1
   0x401039 <_write+27>:	syscall 
   0x40103b <_write+29>:	ret    
   
   0x40103c <_exit>:		mov    eax,0x3c
   0x401041 <_exit+5>:		syscall
--------------------------------------------------


