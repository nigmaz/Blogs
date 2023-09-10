# Reverse-Engineering

- RE Android
- Decompile GCC, Clang và MSVC
    * IDA: decompiler cho C/C++/Golang
    * jadx: decompiler cho Java
    * dnSpy: decompiler cho C#
- RVA (Relative Virtual Address) is an address relative to the base address of the program, an address at which the executable was loaded (where its MZ signature can be found). Any its `VA = base address + RVA`.

![baseAddress.jpeg](./images/baseAddress.jpeg)

- ...

## [0] Overview

- `Course:`
    * https://p.ost2.fyi/courses/course-v1:OpenSecurityTraining2+RE3011_re_cpp+2022_v1/about
    * [crackmes.one](https://crackmes.one/) .

- `Thực hành:` 
  * [IDA-kienmanowar](https://kienmanowar.wordpress.com/category/ida-pro-section/ida-tutorials/) .
  * [PE Analysis Report](https://hackmd.io/@antoinenguyen09/Hy0a2mb0t?fbclid=IwAR0zotdKiVJV-22nlqlGds9YOtvsE08MiKU-zMD8S1urx2mdYZC4nRk2BfQ) .
  * [Assemble-Reverse](https://0xinfection.github.io/reversing/) .

- `Tools:`
  * [Cpp=>Assemble](https://godbolt.org/) .
  * https://microcorruption.com/debugger/Hanoi

- `Writeup Reverse CTF:`
   * https://blog.anhtv.live/2023/07/10/cookie-arena-ss2/
   * [Flare-on 9](https://nextheia.com/tags/flare-on-9-write-up/) .
   * https://github.com/fareedfauzi/Flare-On-Challenges
   * https://0ji54n.netlify.app/works/flareon9 .
   * [ASCIS 2022 - Faku](https://mochinishimiya.github.io/posts/ascis2022/?fbclid=IwAR1uNY6kSbsKBoyvQmbepMpdYjdBlOhfnY4yi9Hfs_ZAFJUalFQUTOZLjqA) .
   * [ISITDTU CTF 2018 Quals - inter](https://aides2593.github.io/writeup/re/2018/08/21/inter.html) .
   * https://hackmd.io/Egk1bvxQTXCG1Tvkk2MNkg#REVERSE
    

- `References:`
    * [Slide SVATTT - RE b2](https://docs.google.com/presentation/d/1SBBp04TkILxE-vSARvI_Uo3aF7lswh-FT5dumWWssT0/edit?fbclid=IwAR33UPvpYYBkpxZL8qfOJ2V-XF6xxFhE5BRuVnrNZGVkLGHT2U0i1f-iOio#slide=id.g241d1437ad9_0_0) .
    * **Machine RE**
        + Windows-10 + https://github.com/mandiant/flare-vm .
        + [GNU Linux](https://remnux.org/?fbclid=IwAR3LEPYLKkJWe2rwHav8pwY9igS5e89p3q0sqFy8_ZNvkio-WHRRV99GjhA) .
        + [RE-Toolkit](https://github.com/mentebinaria/retoolkit?fbclid=IwAR1uAu_jBCIVc1y57PSv6xesm4Nedmw6ai23Nj-a58HxwDuSFNG4AcZVJA0) .
        + [LAB Tryhackme](https://tryhackme.com/room/windowsreversingintro?fbclid=IwAR3yC6T0hFYake1O9dIrP13sAlKdOxC2JJkXH79047LbxwHdmCQqjEOF1Jo) .
    * **AntiDebug**
        + https://users.cs.utah.edu/~aburtsev/malw-sem/slides/02-anti-debugging.pdf
        + https://www.apriorit.com/dev-blog/367-anti-reverse-engineering-protection-techniques-to-use-before-releasing-software#p4
        + https://www.veracode.com/blog/2008/12/anti-debugging-series-part-i
        + https://anti-debug.checkpoint.com/
        + **Questions:** exception, debugger là gì ?
- `Lab:`
   * https://github.com/wtsxDev/reverse-engineering
   * https://github.com/mytechnotalent/Reverse-Engineering
   * https://github.com/michalmalik/linux-re-101
   * https://github.com/michalmalik/osx-re-101
## [1]. Cryptography
- Crypto (Dreamhack)
- https://cryptohack.org/courses/
- https://cryptopals.com/

## [2]. Forensics - Threat Hunting
- Tools forensics VM   * https://github.com/1259iknowthat/ForVM
  
- Dump Memory Tools:
  * https://github.com/volatilityfoundation/volatility
  * https://github.com/volatilityfoundation/volatility/wiki/Command-Reference
  * Convert snapshot file => file.vmem https://kb.vmware.com/s/article/2003941

- `CTF>` BKsec-memorydump: https://gist.github.com/1259iknowthat/8cb818f0a37566b1fc25151ef074d9af
- https://vmtien.id.vn/phan-0-tong-quan-ve-digital-forensics-lab-vncert-cc/
- https://labs.jumpsec.com/no-logs-no-problem-incident-response-without-windows-event-logs/

 
