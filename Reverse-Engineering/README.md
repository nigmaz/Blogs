# Reverse-Engineering

- RVA (Relative Virtual Address) is an address relative to the base address of the program, an address at which the executable was loaded (where its MZ signature can be found). Any its `VA = base address + RVA`.
- File PE 32-bit có chữ `'L'` or `'I'` đằng sau PE Signature, PE 64-bit có chữ `'dt'` đằng sau PE signature.

  - IMAGE_OPTIONAL_HEADER32/Magic: 0x10B cho 32bit.
  - IMAGE_OPTIONAL_HEADER32/Magic: 0x20B cho 64bit.

- `Tools:`

  - [Cpp=>Assemble](https://godbolt.org/) .
  - https://microcorruption.com/debugger/Hanoi

- ...

## [0]. Overview

- https://fareedfauzi.gitbook.io/ctf-playbook/reverse-engineering
- https://0xinfection.github.io/reversing/ .
- `kienmanowar`:

  - https://kienbigmummy.medium.com/
  - [IDA-kienmanowar Blogs](https://kienmanowar.wordpress.com/category/ida-pro-section/ida-tutorials/) .

- `Course:`

  - CTF: https://crackmes.one/
  - CTF: http://reversing.kr/
  - https://beginners.re/paywall/
  - https://opensecuritytraining.info/Training.html

### [A]. Anti-Debugging

- `NOTE`:
  - https://anti-debug.checkpoint.com/
  - https://users.cs.utah.edu/~aburtsev/malw-sem/slides/02-anti-debugging.pdf
- https://www.apriorit.com/dev-blog/367-anti-reverse-engineering-protection-techniques-to-use-before-releasing-software#p4

### [B]. Anti-Disassembly

- ...

### [C]. Anti-Virtual Machine Techniques

- ...

### [D]. Packers and Unpacking

- [Pack PE Analysis Report](https://hackmd.io/@antoinenguyen09/Hy0a2mb0t?fbclid=IwAR0zotdKiVJV-22nlqlGds9YOtvsE08MiKU-zMD8S1urx2mdYZC4nRk2BfQ) .
- https://github.com/unipacker/unipacker

### [E]. Reverse Cpp

- https://p.ost2.fyi/courses/course-v1:OpenSecurityTraining2+RE3011_re_cpp+2022_v1/about

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

## [1]. Malware:

```ps1
certutil -hashfile <ten-file> <hash-type>
```

- https://xikhud.wordpress.com/

- Dev malware quynx: https://maldevacademy.com/syllabusa

- CS6038/CS5138- https://class.malware.re/

- Malware-Repo - https://github.com/Da2dalus/The-MALWARE-Repo

- `Paper Analysis`:

  - https://whitehat.vn/threads/chien-dich-aurora-va-cuoc-chien-ngam-tren-khong-gian-mang-giua-hai-sieu-cuong-phan-1.17333/
  - https://whitehat.vn/threads/phan-tich-ma-doc-windows-co-ban-phan-i.16951/
  - https://anonyviet.com/minh-da-bypass-av-xam-nhap-windows-10-voi-metasploit-va-python-nhu-the-nao/
  - https://github.com/matro7sh/BypassAV
  - https://anonyviet.com/hacker-an-malware-vao-hinh-anh-va-thuc-thi-nhu-the-nao

- `References`:
  - [How Does Malware Know It's Being Monitored?](https://www.youtube.com/watch?si=0lbLFGG9dlPLZ3PJ&v=5cch_-3NVLk&feature=youtu.be).
  - https://www.ired.team/offensive-security/code-injection-process-injection/backdooring-portable-executables-pe-with-shellcode
  - https://github.com/erfan4lx/Windows-Virus
  - https://www.youtube.com/watch?v=eiT7mslA63c
  - Video WannaCry:
    - https://www.youtube.com/watch?si=gEm193iR5BD4bV-M&v=Sv8yu12y5zM&feature=youtu.be
    - https://github.com/Da2dalus/The-MALWARE-Repo/blob/master/Ransomware/WannaCry.exe
  - ...

[+] [Russian Hacker video demo attack](https://www.youtube.com/watch?v=CV39QzFpJx4)

## [2]. References:

- **RE-Machine**:
  - [Windows-10 + flare-vm](https://github.com/mandiant/flare-vm) .
    - [RE-Toolkit Windows](https://github.com/mentebinaria/retoolkit) .
  - [Linux-Distribution + REMnux](https://remnux.org/) .
- ...
