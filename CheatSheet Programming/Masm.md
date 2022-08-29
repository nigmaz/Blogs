# MASM
>Setup `Visual Studio 2019` code and debug `Masm`.

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
>External Include Directories: `;C:\masm32`.

-----------------------------------------------

[+] [Video Tutorial](https://www.youtube.com/watch?v=9e1ER2o83N0&list=PL2YJKKcudhJ0ar-IYMehPGRwbcUz8NZJj&index=19&t=11s) .
      

      
