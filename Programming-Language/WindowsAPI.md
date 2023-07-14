# WindowsAPI

> VisualStudio-2019. WindowsAPI (language C or Cpp) settings project Type: `Empty project`.

- Learn: `learn mfc` - https://functionx.com/visualc/index.htm.

## [0]. NOTE:

- config VS 2019 - {Name project} => Properties => Linker => System => SubSystem : `Windows (/SUBSYSTEM:WINDOWS)` .

- run in VS 2019 - fix chinese characters: [add utf-8 into Character Set](https://learn.microsoft.com/en-us/cpp/build/reference/utf-8-set-source-and-executable-character-sets-to-utf-8?view=msvc-170#set-the-option-in-visual-studio-or-programmatically) .


- C4133 error visual studio 2019 from 'LPWSTR' to 'LPCSTR', FIX:
     * To compile your code in Visual C++ you need to use Multi-Byte char WinAPI functions instead of Wide char ones.
     * Set Project -> Properties -> Advanced (or. General for older versions) -> Character Set option to Use Multi-Byte Character Set

- x64 change `Solution Platforms` => x64 / set [1] NOTE .


## [1]. Knowledge:

* Base Services - kernel32.dll 
* Advance Services - dvapi32.dll
* Graphics Services - gdi32.dll
* User Interface - shell32.dll, user32.dll, comctl32.dll, comdlg32.dll
* Network Service and Multimedia 

## [2] References:

[+] learn Win32 - [Document](http://www.winprog.org/tutorial/start.html) .

[+] code WinAPI + ASM [Ref](https://www.youtube.com/watch?v=pdgmlto7Uwc) .

[+] [Video Tutorial](https://www.youtube.com/watch?v=yvWYggka30A) .

[+] [List video WinAPI - MFC Programming](https://www.youtube.com/watch?v=60O6B2Di5RE&list=PLfszubEEhakf7mGTDjsImyp-YGU69_S5k&index=42) .







      

      
