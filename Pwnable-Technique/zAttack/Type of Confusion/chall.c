// gcc chall.c -o chall -Wl,-z,relro -fstack-protector-all -no-pie
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// #include "main.h"
#define ARRAY_SIZE 100000

const static char *flagString = "giveMeTheFlagPLS";

bool existsInString(char *needle, char *buf)
{
    return strstr(buf, needle);
    // strstr return *address string but this function return boolean
}

void invalidInput()
{
    printf("no hacking pls!!!1111!\n");
    exit(-1);
}

int main()
{
    char *buf = malloc(ARRAY_SIZE);
    printf("prepare to write to buffer at: %p\n", buf);
    printf("please enter your super secret string: ");
    fflush(stdout);
    fgets(buf, ARRAY_SIZE, stdin);
    // b *main+122
    if (existsInString(flagString, buf)) // condition 1 
    {
        printf("only admins are allowed to use the 'super secret' string\n");
        invalidInput();
    }
    // dieu kien long nhau de filter du true hay false
    if (strstr(buf, flagString)) // condition 2
    {
        printf("welcome, you must be an admin!\n");
        FILE *flagFile = fopen("flag.txt", "r");
        if (flagFile == NULL)
        {
            fprintf(stderr, "error opening flag file, please contact an administrator (this is not part of the challenge)\n");
            exit(-1);
        }
        fgets(buf, ARRAY_SIZE, flagFile);
        printf("here's your flag... %s\n", buf);
    }
    else
    {
        printf("hmm, seems you don't know the secret phrase -- you're probably not supposed to be here :)\n");
    }
    free(buf);
}
