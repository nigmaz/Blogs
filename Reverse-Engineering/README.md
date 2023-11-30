# Reverse-Engineering

- RVA (Relative Virtual Address) is an address relative to the base address of the program, an address at which the executable was loaded (where its MZ signature can be found). Any its `VA = base address + RVA`.
- File PE 32-bit có chữ `'L'` or `'I'` đằng sau PE Signature, PE 64-bit có chữ `'dt'` đằng sau PE signature.
  - IMAGE_OPTIONAL_HEADER32/Magic: 0x10B cho 32bit.
  - IMAGE_OPTIONAL_HEADER32/Magic: 0x20B cho 64bit.
```ps1
certutil -hashfile <ten-file> <hash-type>
```
- ...

## [0] Overview
- https://fareedfauzi.gitbook.io/ctf-playbook/reverse-engineering
- `Course:`
    * https://p.ost2.fyi/courses/course-v1:OpenSecurityTraining2+RE3011_re_cpp+2022_v1/about
    * [crackmes.one](https://crackmes.one/) .

- `Thực hành:` 
  * [IDA-kienmanowar](https://kienmanowar.wordpress.com/category/ida-pro-section/ida-tutorials/) .
  * [Pack PE Analysis Report](https://hackmd.io/@antoinenguyen09/Hy0a2mb0t?fbclid=IwAR0zotdKiVJV-22nlqlGds9YOtvsE08MiKU-zMD8S1urx2mdYZC4nRk2BfQ) .
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
   * https://knightz1.github.io/blog/?fbclid=IwAR2u4ZJvxEFvaGAcgSwZVRrc2a7UPQz8d3ExOP0vCSwTJZwFGVEVLu8viK8_aem_ATRFVrLxZKGJHRksRAr0yU7rUTq8lqlSuItH9V4Impev2IVselV1RbeaPWmnbK-UlKI


- `Lab:`
   * https://github.com/wtsxDev/reverse-engineering
   * https://github.com/mytechnotalent/Reverse-Engineering
   * https://github.com/michalmalik/linux-re-101
   * https://github.com/michalmalik/osx-re-101


## [2]. References:

- **RE-Machine**:
   * [Windows-10 + flare-vm](https://github.com/mandiant/flare-vm) .
     + [RE-Toolkit Windows](https://github.com/mentebinaria/retoolkit) .
   * [Linux-Distribution + REMnux](https://remnux.org/) .
- ...


 
