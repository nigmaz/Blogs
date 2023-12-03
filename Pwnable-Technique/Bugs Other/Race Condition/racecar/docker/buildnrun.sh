#!/bin/sh

sudo docker build . -t racecar && sudo docker run --rm -p 10002:10002 -it racecar