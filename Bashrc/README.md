# ~/.bashrc

NOTE: If you use zsh then add it into ~/.zshrc

### ALIAS

```
# ASLR
alias check_aslr='cat /proc/sys/kernel/randomize_va_space'

alias turn_off_aslr="echo 0 | sudo tee /proc/sys/kernel/randomize_va_space"

alias turn_on_aslr="echo 2 | sudo tee /proc/sys/kernel/randomize_va_space"
```

### NASM

neofetch | lolcat

figlet -f smslant "l1j9m4 0n1"

```
# nasm -f elf helloworld.asm && ld -m elf_i386 helloworld.o -o helloworld && ./helloworld
# cnasm32 <file.asm>
cnasm32(){
    filename=${1%.*}
    nasm -f elf $filename.asm; ld -m elf_i386 $filename.o -o $filename #; ./$filename
}
```

```
# nasm -f elf64 hello.asm && ld hello.o -o hello && ./hello
# cnasm64 <file.asm>
cnasm64(){
    filename=${1%.*}
    nasm -f elf64 $filename.asm; ld $filename.o -o $filename #; ./$filename
}
```

### ADD PYTHON INTO PATH

```
# PYTHON write into ~/.bashrc or ~/.zshr
export PATH="$HOME/bin:/usr/lib/python3:/usr/local/lib/python2.7:$PATH"
```

### NOTE: `source ~/.bashrc` or `source ~/.zshrc`.

Loading...
