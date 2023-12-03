#!/bin/sh

cd /home/user
socat tcp-listen:10002,fork,reuseaddr exec:./racecar 2>/dev/null