# Windows

![version.png](./version.png)

- Tùy từng tường hợp demo cái gì trên máy ảo windows kiểu rce back reverseshell thì tắt hết firewall đi (chỉ thực tập cơ sở thôi).
- Fix [Antimalware Service Executable hight CPU](https://www.freecodecamp.org/news/what-is-antimalware-service-executable-why-is-it-high-cpu-disk-usage/#:~:text=Antimalware%20service%20executable%20is%20a%20Windows%20Security%20process%20that%20executes,programs%20from%20time%20to%20time.) .

## [1]. Windows install and setup

### A) Active Windows and Office

- Chỉ sử dụng trên máy ảo (Trong google drive có office).
- [Office2016](https://drive.google.com/drive/folders/1VgZRlnU4GvfcmqUW-ms4rfqrqiQIZJsB?usp=sharing) .
- [Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts/releases) . 


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
- Text Editor | IDE:
  * Visual Studio*
  * Dev C++
  * Sublime Text
- Demo CVE:
  * Process Hacker 2
  * WireShark

## [3]. NOTE
  * https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite
  * [SublimeText config](https://github.com/NigmaZ/Blogs/tree/main/Virtual-Machine/Note/Sublime%20config) .
