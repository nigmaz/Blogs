# Kernel Source setup

## [1]. compile kernel source setup qemu debug

>Source kernel download: https://mirrors.edge.kernel.org/pub/linux/kernel/, chọn version v< number >.x, xong thay tên branch mình muốn.

VD: https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.15.4.tar.xz


```bash
sudo apt-get install build-essential libncurses-dev bison flex libssl-dev libelf-dev

# qemu-system-x86_64 -kernel git/kernel/linux/arch/x86_64/boot/bzImage -initrd ramdisk.img -s -append "console=ttyS0" -nographic

```

> Reference:

[+] [Build and module initrd.img](https://kviccn.github.io/posts/2021/08/linux-%E5%86%85%E6%A0%B8%E7%BC%96%E8%AF%91%E5%8F%8A%E8%BF%90%E8%A1%8C/)

```bash
(initramfs) ls
dev      bin      init     lib64    sbin     var      tmp
root     conf     lib      libx32   scripts  sys
kernel   etc      lib32    run      usr      proc
(initramfs)
```

[+] https://www.sobyte.net/post/2022-02/debug-linux-kernel-with-qemu-and-gdb/

[+] https://pnx9.github.io/thehive/Debugging-Linux-Kernel.html

[+] https://www.sobyte.net/post/2022-02/debug-linux-kernel-with-qemu-and-gdb/

[+] [get bzImage-cn](https://kviccn.github.io/posts/2021/08/linux-%E5%86%85%E6%A0%B8%E7%BC%96%E8%AF%91%E5%8F%8A%E8%BF%90%E8%A1%8C/)

http://trac.gateworks.com/wiki/buildroot

https://bootlin.com/pub/conferences/2013/kernel-recipes/rootfs-kernel-developer/rootfs-kernel-developer.pdf


> Change kernel OS 

* [Thay đổi version kernel - VI](https://viblo.asia/p/xay-dung-linux-kernel-va-them-loi-goi-he-thong-vao-linux-kernel-aAY4qvzeJPw) .

* [Video build change kernel in OS](https://www.youtube.com/watch?v=cAWqWB2wVZc) .

* [Video Change kernel OS from compile source code kernel](https://www.youtube.com/watch?v=E4yRcmQqvWM) . 

> Video 

2.

[+] [How to build Linux Kernel from sources](https://www.youtube.com/watch?v=1gEFYoGUFxM&t=30s) .

> Add syscall kernel module

https://dev.to/jasper/adding-a-system-call-to-the-linux-kernel-5-8-1-in-ubuntu-20-04-lts-2ga8?fbclid=IwAR32uePGNxcGYK8XaI20-CQjxh23BCaY8AHkrrcaqDrO60QSDzBte3-749A

https://viblo.asia/p/xay-dung-linux-kernel-va-them-loi-goi-he-thong-vao-linux-kernel-aAY4qvzeJPw?fbclid=IwAR2TKkIegW2_AO663yw60SjwcRWP-bQsYTWmbRsMa1ldRJU0TewuIbQ6N-s

__VI__

[+] [Nâng cấp kernel OS linux-vi](https://cloudcraft.info/huong-dan-upgrade-kernel-linux/)

[+] [Điều gì xảy ra khi boot mot he thong linux](https://cloudcraft.info/nhung-gi-da-xay-ra-khi-boot-mot-he-thong-linux/)

## [2]. 0-days, 1-days and n-days, ...

> Kernel source

  * https://www.kernel.org/

  * https://github.com/torvalds/linux

> Kernel - CTF: 

* https://blog.efiens.com/post/midas/linux-kernel-pwn-1/

* https://lkmidas.github.io/posts/20210123-linux-kernel-pwn-part-1/

* https://x3ero0.tech/posts/easy_kernel_exploitation/

* https://y3a.github.io/2021/06/11/hxpctf-kernelrop/

* https://uaf.io/exploitation/2018/12/30/HOWTO-make-kernel-pwns.html?fbclid=IwAR1W2W87bhH5HeW2M5T-i2gu3XfhnEstidish_X7fdosknhiLz7CE085HNA

* https://2020.ctf.link/

* https://2021.ctf.link/

* https://2022.ctf.link/

* https://hackmd.io/@avila-pwn-notes/Hy1_8uzuY#Final-Payload

> CVE - [RCE, PLE]:

* https://0x434b.dev/

* https://www.freebuf.com/vuls/197122.html?fbclid=IwAR1HW1ATrcUYxFqAhCNaxBkm0BykAyVp7e7nVfFmhCvef8zlPvRnYhWZ6Jo

* https://securityonline.info/poc-code-for-linux-kernel-privilege-escalation-flaw-cve-2022-2602-published/?fbclid=IwAR2ATZ_9vrlvg5Sy1PWmK5fFkmOwamw9Fjy6u4HogmJ1IK27TRnflyop0-E

> Video:

* https://www.youtube.com/watch?v=HtdriW7KVNE

* https://www.youtube.com/playlist?list=PLiCcguURxSpbD9M0ha-Mvs-vLYt-VKlWt

* https://youtu.be/EoU3sXP2IH8 

* https://www.youtube.com/watch?v=n0O4Sws01Ro&list=WL&index=252&t=774s

* Tools: PEASS, PEASS Windows, ...

* Documents: https://book.hacktricks.xyz/linux-hardening/privilege-escalation

* [Home Tiếng Việt] https://vimentor.com/en/lesson/gioi-thieu-ve-linux-kernel-1


