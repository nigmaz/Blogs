# Loading...

>Source kernel download: https://mirrors.edge.kernel.org/pub/linux/kernel/, chọn version v< number >.x, xong thay tên branch mình muốn.

VD: https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.15.4.tar.xz


```bash
sudo apt-get install build-essential libncurses-dev bison flex libssl-dev libelf-dev

# qemu-system-x86_64 -kernel git/kernel/linux/arch/x86_64/boot/bzImage -initrd ramdisk.img -s -append "console=ttyS0" -nographic

```

> Reference:

[+] [Upgrade kernel linux-vi](https://cloudcraft.info/huong-dan-upgrade-kernel-linux/)

[+] [Điều gì xảy ra khi boot mot he thong linux](https://cloudcraft.info/nhung-gi-da-xay-ra-khi-boot-mot-he-thong-linux/)

[+] https://pnx9.github.io/thehive/Debugging-Linux-Kernel.html

[+] [get bzImage-cn](https://kviccn.github.io/posts/2021/08/linux-%E5%86%85%E6%A0%B8%E7%BC%96%E8%AF%91%E5%8F%8A%E8%BF%90%E8%A1%8C/)

>Video 

[+] [build change kernel in OS](https://www.youtube.com/watch?v=cAWqWB2wVZc)

[+] [How to build Linux Kernel from sources](https://www.youtube.com/watch?v=1gEFYoGUFxM&t=30s)

[+] [Change kernel OS from compile source code kernel](https://www.youtube.com/watch?v=E4yRcmQqvWM) . 
