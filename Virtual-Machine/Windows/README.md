# Windows

- Tùy từng tường hợp demo cái gì trên máy ảo windows kiểu rce back reverseshell thì tắt hết firewall đi (chỉ thực tập cơ sở thôi).

## [1]. Windows stuff

### A) Active Windows and Office

- Active: run cmd administrator

```bat
Cscript slmgr.vbs -upk
Cscript slmgr.vbs /ckms
Sc config Sppsvc start= auto & Net.exe start Sppsvc
Sc config Osppsvc  start= auto & Net.exe start Osppsvc
sc config LicenseManager start= auto & net start LicenseManager
sc config wuauserv start= auto & net start wuauserv
Cscript slmgr.vbs /ipk VNW26-D6PYF-QK9V8-96XKC-7CFC6
changepk.exe /productkey BGRWH-K2JPJ-VX82X-8CRF8-D43MT
Cscript slmgr.vbs -ato
exit
exit
```

- Office

### B) Turn off Windows Defender

- [turnOffWindowsDefender-Vi](https://www.dienmayxanh.com/kinh-nghiem-hay/huong-dan-cach-tat-windows-defender-trong-win-10-c-1162982#:~:text=B%C6%B0%E1%BB%9Bc%201%3A%20Double%20click%20v%C3%A0o,Real%2Dtime%20protection%20sang%20OFF.)

- [turnOffWindowsDefender-En](https://www.maketecheasier.com/xbox-game-bar-windows/?scr=1)

- Windows10 Home: 

```
`Registry Editor` => `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender` set `DisableAntiSpyware`

0 - On WindowsDefender

1 - Off WindowsDefender
```

### C) Expand disk VM Windows 

- [Expand disk Windows VM](https://www.youtube.com/watch?v=Y5aT8hE177I)

- Shrink Recovery Partition

```bat
cmd> diskpart
disk> select disk 0
disk> select partition 4
disk> delete partition override
```
## [2]. Windows for Exploit
- [WSL](https://bwgjoseph.com/how-to-manually-install-wsl2-on-a-windows-10-virtual-machine) .
  * Virtualization engine => Virtualize Intel VT-x/EPT or AMD-V/RVI

- Hex-Rays IDA Pro 7.7
  * [+] [IDA Pro - English](https://drive.google.com/file/d/1wf2XemQQwzpdSdQic63fZ0pC0829XcDE/view?usp=sharing) .
  * [+] [IDA Pro - China](https://drive.google.com/file/d/1qkMy9u1FVz9uFRa2qfBI7_694iJLe5ZW/view?usp=sharing) .

- WinDBG
- x84_64dbg
- OllyDbg
- Detect It Easy
- CFF Explorer Suite IV
- HxD
- Process Explorer
- Text Editor | IDE:
  * Dev C++
  * Sublime Text | VS Code
- Demo CVE:
  * Process Hacker 2
  * WireShark

## [3]. NOTE
  * https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite
  * [SublimeText config](https://github.com/NigmaZ/Blogs/tree/main/Virtual-Machine/Note/Sublime%20config) .
