# WinAPI

> VS2019. WinAPI (language C) settings project Type: `Empty project`.

### NOTE:

[!] config VS 2019 - {Name project} => Properties => Linker => System => SubSystem : `Windows (/SUBSYSTEM:WINDOWS)` .

[!] run in vs 2019 : [add utf-8 into Character Set](https://learn.microsoft.com/en-us/cpp/build/reference/utf-8-set-source-and-executable-character-sets-to-utf-8?view=msvc-170#set-the-option-in-visual-studio-or-programmatically) .


[!] C4133 error visual studio 2019 from 'LPWSTR' to 'LPCSTR'

      * To compile your code in Visual C++ you need to use Multi-Byte char WinAPI functions instead of Wide char ones.

      * Set Project -> Properties -> Advanced (or. General for older versions) -> Character Set option to Use Multi-Byte Character Set

[!] x64 change `Solution Platforms` => x64 .


-----------------------------------------------

[+] learn Win32 - [Document](http://www.winprog.org/tutorial/start.html) .

[+] [Video Tutorial](https://www.youtube.com/watch?v=yvWYggka30A) .







      

      
