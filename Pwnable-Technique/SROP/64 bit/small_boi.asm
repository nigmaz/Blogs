   0x40017c:	push   rbp
   0x40017d:	mov    rbp,rsp
   
   0x400180:	mov    eax,0xf		; sigreturn() syscall
   0x400185:	syscall 
   
   0x400187:	nop
   0x400188:	pop    rbp
   0x400189:	ret    
   0x40018a:	pop    rax
   0x40018b:	ret    
   
   0x40018c:	push   rbp
   0x40018d:	mov    rbp,rsp
   0x400190:	lea    rax,[rbp-0x20]
   0x400194:	mov    rsi,rax
   0x400197:	xor    rax,rax
   0x40019a:	xor    rdi,rdi
   0x40019d:	mov    rdx,0x200
   0x4001a4:	syscall 		; read string, address in rbp-0x20
   
   0x4001a6:	mov    eax,0x0
   0x4001ab:	pop    rbp
   0x4001ac:	ret    
   
_start:
   0x4001ad:	push   rbp
   0x4001ae:	mov    rbp,rsp
   0x4001b1:	mov    eax,0x0
   0x4001b6:	call   0x40018c
   0x4001bb:	xor    rax,rdi
   0x4001be:	mov    rax,0x3c
   0x4001c5:	syscall 		; exit
   
   0x4001c7:	nop
   0x4001c8:	pop    rbp
   0x4001c9:	ret 
