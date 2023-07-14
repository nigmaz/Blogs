#include <stdio.h>
#include <stdlib.h>

static char* dodgy = "/bin/sh";

void func() {
    __asm__(  // all typical things found via a libc leak, or a large binary
          "mov $0x77, %eax;"
          "ret;"
          "int $0x80"
            );
}
void vuln() {
    printf("Hey look its a cheeky gadget\n");
    printf("func: %p\n", func);
    printf("/bin/sh: %p\n", dodgy);

    char buf[4];
    gets(buf);
}

int main() {
    vuln();
}

