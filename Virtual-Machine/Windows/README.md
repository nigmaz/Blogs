
# Windows
- `Build file install.bat or install.ps1` is loading...
  - 1, 2, 3, 95, 98, NT, 2000, XP, VISTA, 7, 8, 10, 11.
- Tùy từng tường hợp demo cái gì trên máy ảo windows kiểu rce back reverseshell thì tắt hết firewall đi (chỉ thực tập cơ sở thôi).
- Source File .ISO
  - https://docs.google.com/spreadsheets/d/1o5dmOw8jBCVGxFmlMOsKgoIKULMY7tk-TCSz67IJMc4/pubhtml#

## [1]. Windows install and setup

- Trick-in-Windows-setup
  * [Fix Antimalware Service Executable hight CPU](https://www.freecodecamp.org/news/what-is-antimalware-service-executable-why-is-it-high-cpu-disk-usage/#:~:text=Antimalware%20service%20executable%20is%20a%20Windows%20Security%20process%20that%20executes,programs%20from%20time%20to%20time.) .
  * [Windows Server enable wifi](https://www.youtube.com/watch?v=PupMFBL39RI) .

### A) Active Windows and Office
> Chỉ sử dụng trên máy ảo (Trong google drive có office).
- https://voz.vn/t/tong-hop-tien-ich-kich-hoat-all-in-one-windows-office-backup-key-cap-nhat-03-2023.737622/
- [Office2016 install](https://drive.google.com/drive/folders/1VgZRlnU4GvfcmqUW-ms4rfqrqiQIZJsB?usp=sharing) .
- [Microsoft-(Windows+Office)-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts/releases) . 
- active Windows 7:
  - Service turn off: `Windows Update` and `Software Protection`.
  - cmd: `slmgr -rearm`.

### B) Turn off Windows Defender

- TurnOffWindowsDefender:
  - https://www.youtube.com/watch?v=31TDHRegTLM
  - Task Scheduler -> Edit group policy -> Windows Services

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
- [WSL in Windows-10 and Windows-11](https://learn.microsoft.com/en-us/windows/wsl/install) .
- [WSL](https://bwgjoseph.com/how-to-manually-install-wsl2-on-a-windows-10-virtual-machine) in `Virtual Machine`.
  * Virtualization engine => Virtualize Intel VT-x/EPT or AMD-V/RVI

- `Debugging Tools`
  * Hex-Rays IDA Pro 7.7
    + [IDA Pro - English](https://drive.google.com/file/d/1wf2XemQQwzpdSdQic63fZ0pC0829XcDE/view?usp=sharing) .
    + [IDA Pro - China](https://drive.google.com/file/d/1qkMy9u1FVz9uFRa2qfBI7_694iJLe5ZW/view?usp=sharing) .

  * WinDBG
  * x84_64dbg 
    + [Cheat-sheet](https://gist.github.com/sidharthpunathil/74911917ebc7be6ce13fabe8e3abdf8d) .
  * OllyDbg
- `PE Analysis tools`
  * Detect It Easy
  * CFF Explorer Suite IV 
  * HxD
- `Text Editor | IDE`
  * Visual Studio*
  * Dev C++
  * Sublime Text
- `Process Monitor`
  * Process Hacker 2
  * Process Explorer
- `Logs and check events`
  * Event Viewer (Sysmon + Logs powershell commandline)
  * API monitoring
- `Network monitor`
  * WireShark
 


## [3]. Reeferences:
  * [Windows-Virtual-Machine-for-RE | flare-vm](https://github.com/mandiant/flare-vm) .
  * [Sysinternals-full-tools](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite) .
  * [SublimeText config](https://github.com/NigmaZ/Blogs/tree/main/Virtual-Machine/Note/Sublime%20config) .
  * ...
