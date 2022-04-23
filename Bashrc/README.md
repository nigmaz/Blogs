# ~/.bashrc

NOTE: If you use zsh then add it into ~/.zshrc

### ALIAS

```
alias check_aslr='cat /proc/sys/kernel/randomize_va_space'

alias turn_off_aslr="echo 0 | sudo tee /proc/sys/kernel/randomize_va_space"

alias turn_on_aslr="echo 2 | sudo tee /proc/sys/kernel/randomize_va_space"
```

### NASM

~$ nasm -f elf64 hello.asm && ld hello.o -o hello && ./hello

~$ nasm -f elf helloworld.asm && ld -m elf_i386 helloworld.o -o helloworld && ./helloworld

neofetch | lolcat

figlet -f smslant "l1j9m4 0n1"

```
cnasm32(){
    filename=${1%.*}
    nasm -f elf $filename.asm; ld -m elf_i386 $filename.o -o $filename #; ./$filename
}
```

```
cnasm64(){
    filename=${1%.*}
    nasm -f elf64 $filename.asm; ld $filename.o -o $filename #; ./$filename
}
```

...
