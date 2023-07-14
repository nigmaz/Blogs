#include <stdio.h>

void winner(int x, int y, int z){
    if(z == 0xdeadbeef){
        puts("Awesome work!");
    }
}

int main(){
    puts("Come on then, ret2csu me");

    char input[30];
    gets(input);
    return 0;
}

// gcc ret2csu.c -o ret2csu -fno-stack-protector -no-pie 
