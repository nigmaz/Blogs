# MASM
>Setup `Visual Studio 2019` code and debug `mASM` with lib `masm32` .

### 1) Install masm32

[+] [Library Irvine](https://asmirvine.com/)

[+] [Library masm32](https://www.masm32.com/download.htm)

[+] [Tutorial Install masm32](https://asmdude.wordpress.com/2019/02/15/how-to-install-masm32-on-windows-10/)

- Check `masm32` in `cmd` run: *__ml__*.

### 2) Setting for masm32 in VS2019

[1] Build Dependencies.
- `masm(.targets, .props)`.

[2] Properties/Item Type/Microsoft Macro Assembler.
  
+) Library `Irvine`.

- Linker/Addtional Library Directories: `C:\Irvine`.
- Input/(in First line): `irvine32.lib;...`.
- Microsoft Macro Assembler:\Include Paths: `C:\Irvine`.
   
+) Library `masm32`.
- Properties/VC++ Directories:
`External Include Directories: ";C:\masm32".`

### 3) [loadPEB](https://securitycafe.ro/2015/10/30/introduction-to-windows-shellcode-development-part1/) and `Extern`.

[1] Build Dependencies.
- `masm(.targets, .props)`.

[2] Linker/Advanced/Entry Point.
- `Entry point: => set "main"`.

>NOTE: Check `Item type: Microsoft Macro Assembler` and `Configuration Manager - x64` .

### * Code `mASM` load `PEB - (Process Environment Block)` .

* x86 : point entry load start `main`. set `Build Dependencies` . set `Solution Platforms` .
* x86_64 : point entry load start `mainCRTStartup`. set `Build Dependencies` . set `Solution Platforms` . 

Shellcode Windows:



- Compile: 
 
>`ml /c /Zd /coff msgbox.obj` .

>`link /SUBSYSTEM:CONSOLE  /LIBPATH:c:\masm32\lib  msgbox.obj` . WINDOWS or CONSOLE

-----------------------------------------------

[+] [Video Tutorial](https://www.youtube.com/watch?v=9e1ER2o83N0&list=PL2YJKKcudhJ0ar-IYMehPGRwbcUz8NZJj&index=19&t=11s) .

[+] [Compile masm_x64](https://web.archive.org/web/20140225144938/http://www.codegurus.be/codegurus/Programming/assembler&win64_en.htm) .






      

      
