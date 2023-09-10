FROM ubuntu:22.04

RUN useradd -ms /bin/bash pwn
WORKDIR /home/pwn

ADD pwn1 /home/pwn
ADD flag /home/pwn

RUN chmod 4 /home/pwn/flag
RUN chmod 5 /home/pwn/pwn1

RUN apt-get update -y
RUN apt-get install socat -y

EXPOSE 2007

ENTRYPOINT ["sh", "-c", "exec socat -s TCP-LISTEN:2007, reuseaddr, fork EXEC:/home/pwn/pwn1,stderr"]
