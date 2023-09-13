FROM ubuntu:20.04

RUN apt update && apt install -y socat && apt clean && useradd -m user
ADD share/ /home/user/

WORKDIR /home/user
RUN chmod +x * && chmod 444 flag.txt

USER user
EXPOSE 10002

CMD ["/home/user/run.sh"]