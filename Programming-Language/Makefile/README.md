# Makefile

### Make: use cmd linux `make` compile filename Makefile contain cmd build program.

```bash
EXAMPLES
Example-1:

To Build your programs:

$ make

output:

 gcc -c -Wall test1.c
 gcc -c -Wall test2.c
 gcc -Wall test1.o test2.o -o test 

Note: make reads makefile present in current directory and executes based on statements in makefile
Example-2:

To clean all the object files:

$ make clean

output:

 rm -rf *.o test
Example-3:

 To forcibly build all programs, use -B option:

$ make -B

output:

 gcc -c -Wall test.c
 gcc -c -Wall anotherTest.c
 gcc -Wall test.o anotherTest.o -o test
Example-4:

To run make in debug mode, use the -d option :

$ make -d

output:

Copyright (C) 2006 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
This program built for x86_64-pc-linux-gnu

Reading makefiles...
Reading makefile `Makefile'...
Updating makefiles....
Considering target file `Makefile'.
Looking for an implicit rule for `Makefile'.
Trying pattern rule with stem `Makefile'.
Trying implicit prerequisite `Makefile.o'.
Trying pattern rule with stem `Makefile'.
Trying implicit prerequisite `Makefile.c'.
Trying pattern rule with stem `Makefile'.
Trying implicit prerequisite `Makefile.cc'.
Trying pattern rule with stem `Makefile'.
Trying implicit prerequisite `Makefile.C'.
Trying pattern rule with stem `Makefile'.
Trying implicit prerequisite `Makefile.cpp'.
Trying pattern rule with stem `Makefile'.
--More--
Example-5:

To build programs present in different directory:

$ make -C /home/testdir/

output:

make: Entering directory `/home/himanshu/practice/make-dir'
make: Nothing to be done for `all'.
make: Leaving directory `/home/himanshu/practice/make-dir'
Example-6:

To use other file instead of default makefile, use -f option :

$ make -f my_makefile

output:

gcc -c -Wall test1.c
gcc -c -Wall test2.c
gcc -Wall test1.o test2.o -o test 
```

