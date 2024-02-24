# Reverse-Engineering

- `Tools:`

  - [Cpp=>Assemble](https://godbolt.org/) .
  - https://microcorruption.com/debugger/Hanoi
  - https://github.com/tandasat/scripts_for_RE

- ...

## [0]. Overview

- https://fareedfauzi.gitbook.io/ctf-playbook/reverse-engineering
- https://0xinfection.github.io/reversing/ .
- https://ctf-wiki.mahaloz.re/reverse/windows/anti-debug/int-3/
- `kienmanowar`:

  - https://kienbigmummy.medium.com/
  - [IDA-kienmanowar Blogs](https://kienmanowar.wordpress.com/category/ida-pro-section/ida-tutorials/) .

- `Course:`

  - CTF: https://crackmes.one/
  - CTF: http://reversing.kr/
  - https://beginners.re/paywall/
  - https://opensecuritytraining.info/Training.html

### [A]. Anti-Disassembly

- https://docs.google.com/presentation/d/1SBBp04TkILxE-vSARvI_Uo3aF7lswh-FT5dumWWssT0/edit#slide=id.ge1d838b627_4_19
- Thay đổi các byte không bao giờ được sử dụng như 0xE8, 0xE9, 0xEB thành 0x90 (NOP).
- Các `JUMPOUT` trong IDA là nó nhảy đến bytecode không hợp lệ hoặc do control flow phức tạp quá nên IDA không phân tích được.
- Khi sửa giá trị EIP trong IDA để nhảy lung tung cũng phải chỉnh stack vs register nếu cần cho chuẩn và không để bị lỗi.
- `VM-Protecter`:
  - ...

### [B]. Anti-Debugging

- `NOTE`:
  - https://anti-debug.checkpoint.com/
  - https://users.cs.utah.edu/~aburtsev/malw-sem/slides/02-anti-debugging.pdf
  - https://www.apriorit.com/dev-blog/367-anti-reverse-engineering-protection-techniques-to-use-before-releasing-software#p4

- `Kỹ thuật phân tích`:
  - `Static`: Phân tích code và viết script decrypt để phân tích rồi tìm chỗ nào quan trọng để debug nhằm lấy data hoặc phân tích hành vi.
  - `Dynamic`: Debug và sử dụng cách bypass các kỹ thuật antidebug để đi đến follow chương trình mà muốn thực thi và phân tích (Nếu gặp mẫu nào malware dài thì debug sẽ rất lâu và khó).

- Một số dạng bài:
  - Chương trình sẽ tự decrypt bytecode lúc chạy để check input.
  - ...

### [C]. Anti-Virtual Machine Techniques

- https://github.com/hzqst/VmwareHardenedLoader
- ...

### [D]. Packers and Unpacking

- `Tools`: https://github.com/unipacker/unipacker
- https://github.com/VNSecurityResearch/anm/blob/master/Aspr2.XX_unpacker_v1.15E.osc

### [E]. Reverse Cpp

- https://p.ost2.fyi/courses/course-v1:OpenSecurityTraining2+RE3011_re_cpp+2022_v1/about
- https://mahaloz.re/dec-history-pt1

### [F]. Reversing Other Platform

- `.Net`: file.cs, flie.vbs, file.dll,...

  - VBScript & ILSpy Analysis of a RAT: https://youtu.be/44Yr_E_xAwg?si=zjKSMNz-yu9bXcrC
  - [Tools] Hướng dẫn sử dụng windbg phân tích rootkit: https://youtu.be/PaeQC1c5uVk?si=gYzGWhvssHq_L1N1

- `Android`: file.apk

  - https://nusgreyhats.org/posts/writeups/introduction-to-android-app-reversing/
  - https://itzone.com.vn/vi/article/tim-hieu-dang-ctf-reverse-android-dich-nguoc-va-patch-file-apk/

- `Python`

  - pyinstaller and pydumpck unpacker.

- `ARM architectures`

  - https://github.com/mytechnotalent/Reverse-Engineering
 
- `Golang`
  - https://github.com/0xjiayu/go_parser
## [1]. Malware:

```ps1
certutil -hashfile <ten-file> <hash-type>
```

- https://xikhud.wordpress.com/

- https://samsclass.info/126/126_S16.shtml

- Dev malware quynx: https://maldevacademy.com/syllabusa

- CS6038/CS5138- https://class.malware.re/

- Malware-Repo - https://github.com/Da2dalus/The-MALWARE-Repo

- `Paper Analysis`:

  - https://whitehat.vn/threads/chien-dich-aurora-va-cuoc-chien-ngam-tren-khong-gian-mang-giua-hai-sieu-cuong-phan-1.17333/
  - https://whitehat.vn/threads/phan-tich-ma-doc-windows-co-ban-phan-i.16951/
  - https://anonyviet.com/minh-da-bypass-av-xam-nhap-windows-10-voi-metasploit-va-python-nhu-the-nao/
  - https://github.com/matro7sh/BypassAV
  - https://anonyviet.com/hacker-an-malware-vao-hinh-anh-va-thuc-thi-nhu-the-nao
  - https://security.stackexchange.com/questions/252595/detect-what-antivirus-installed-on-windows-operating-system

- `References`:
  - [How Does Malware Know It's Being Monitored?](https://www.youtube.com/watch?si=0lbLFGG9dlPLZ3PJ&v=5cch_-3NVLk&feature=youtu.be).
  - https://www.ired.team/offensive-security/code-injection-process-injection/backdooring-portable-executables-pe-with-shellcode
  - https://github.com/erfan4lx/Windows-Virus
  - https://www.youtube.com/watch?v=eiT7mslA63c
  - Video WannaCry:
    - https://www.youtube.com/watch?si=gEm193iR5BD4bV-M&v=Sv8yu12y5zM&feature=youtu.be
    - https://github.com/Da2dalus/The-MALWARE-Repo/blob/master/Ransomware/WannaCry.exe

- `Scenario`:
  - https://noventiq.com/security_blog/detecting-guloaders-infection-chain-with-microsoft-sentinel
 
- `Bypass anti-virus`:
  - https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9312198
- ...

[+] [Russian Hacker video demo attack](https://www.youtube.com/watch?v=CV39QzFpJx4)

## [2]. References:

- **RE-Machine**:
  - [Windows-10 + flare-vm](https://github.com/mandiant/flare-vm) .
    - [RE-Toolkit Windows](https://github.com/mentebinaria/retoolkit) .
  - [Linux-Distribution + REMnux](https://remnux.org/) .
- ...
