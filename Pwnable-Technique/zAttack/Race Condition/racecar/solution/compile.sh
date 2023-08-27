#!/bin/sh

gcc -no-pie -fno-stack-protector solution/racecar.c -o racecar -lpthread
cp racecar player
cp racecar docker/share
