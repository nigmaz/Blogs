# Docker

- Docker là một platform cung cấp cho người dùng những công cụ và service để có thể building, deploying và running ứng dụng dễ dàng hơn bằng cách sử dụng các containers (trên nền tảng ảo hóa).

```bash
[DOCKER FILE]=(build) ==> [Image]=(run) ==> [Containers]  
```

- `Docker Registry` : Nơi chứa các Docker Image.
  
- `Docker Compose` : là công cụ cho phép chạy `Ứng Dụng` với nhiều Docker Containers một cách nhanh chóng và dễ dàng.

- Kiểm tra dịch vụ đang hoạt động.

```bash
sudo service docker status
```  

## [1]. Use the Docker command line

### A. BUILD IMAGES:

- Dấu `"."` là chỉ thư viện mình đang hoạt động __(pwd - ý là Dockerfile tại ./)__.
```bash
sudo docker build . -t <tag_name-lower> 
```

- Liệt kê các images đã build __(Khi chạy 1 image => 1 container)__.

```bash
sudo docker images -a 
```

- Xóa images đã build.

```bash 
sudo docker rmi <tag_name/ID_image>
```

### B. RUN IMAGE:

- Chạy container từ image đã build.

```bash
sudo docker run --rm -p <hots-port>:<docker-port> -it <tag_name/ID_image>
```

- Chú thích:
    * `-p` : chỉ định port kết nối trong đó
        + `host-port` là port mà host sẽ listen - khi nc sẽ nc theo cái này.
        + `docker-port` là port mà docker sẽ listen - cái này đi kèm trong dockerfile.
    * --rm : tự động xóa vùng chứa khi thoát.
    * -d : là chạy nền - tùy chọn này thêm cũng được.
    
- Liệt kê các container đang chạy, có cả port listen tcp.

```bash
sudo docker ps -a 
```

- Thực thi câu lệnh yêu cầu với container đã run __(VD như lấy shell vào tương tác với container)__.

- `__[+] NOTE:__ <cmd>` - pwd, /bin/bash, bash, sh, ...

```bash 
sudo docker exec -it <ID_container> <cmd> 
```

- Dừng container đang chạy (dù đã `ctrl + c` câu lệnh nhưng container chạy ngầm).

```bash
sudo docker stop <name_container/ID_container>
```

- Xóa container.

```bash
sudo docker rm <name_container>
```

### C. STOP ALL:

- Stop all running containers.
```bash
sudo docker stop $(sudo docker ps -a -q)
```

- Delete all stopted containers.
```bash
sudo docker rm $(sudo docker ps -a -q)
```

- Delete all image.
```bash
sudo docker rmi $(sudo docker images -q)
```

- Xóa tất cả image và tài nguyên không sử dụng.
```bash 
sudo docker system prune
```

## [2]. The special case

### A. Image github.com/redpwn/jail

- Là 1 form image phổ biến cho CTF.

```bash
FROM pwn.red/jail
```

- Một số lưu ý:
    * __redpwn port default 5000__.
    * Nếu có chỉ định riêng trong file là dòng: __ENV JAIL_PORT = 1337__.
    * Khi chạy container thì thêm tham số __--privileged__.
```bash
sudo docker run --rm -p 5000:5000 --privileged -it <tag_name>
```

### B. Image Docker-compose

- Nếu bài cho 3 file:
    * Dockerfile
    * docker-compose.yml
    * xientd.conf

- Lệnh với docker-compose (tự động chạy lệnh build và run).

```bash
sudo docker-compose up --build
```

- Lệnh `docker-compose <ID_container>` thay bằng tên service trong file.yml

### C. The LIBC in Docker

- Khi cho docker là cho môi trường server => có thể lấy LIBC và LD.

- Cách lấy LIBC:
    * `1.` nc => container đang run.
    * `2.` Lấy id-process của service đang chạy (VD: container chạy chương trình source thì service là source).
    * Lưu ý là một số bài có timeout nên cần thao tác nhanh để `sudo gdb -p id_process`
    ```bash
    ps aux | grep <service>
    ```
    * `3.` Dùng gdb tìm `info proc map` của chương trình đang chạy để tìm path của LIBC trên container.
    ```bash
    sudo gdb -p <id_process>
    ```
    * `4.` Lưu ý: Trường hợp cần tìm xem vị trí bắt đầu ở đâu (trong Docker file chỉ định nơi bắt đầu work - pwd) sau đó mới đến path tìm được từ gdb - __[/srv/usr/lib]__ OR __[/usr/lib]__ 
        + Lấy LIBC
        ```bash
        sudo docker cp <container_id>:/path_libc .
        ```
        + Lấy LD
        ```bash
        sudo docker cp <container_id>:/path_ld .
        ```
        + Phân quyền
        ```bash
        sudo chown nigmaz libc.so.6 ld-linux-x86-64.so.2
        ```

### D. WSL

- Đối với WSL, để chạy được lệnh docker cần chạy nền docker daemon với lệnh sau: __sudo dockerd &__ rồi mới đến các câu lệnh đã liệt kê.

- Một số vị trí nhận biết port
    * __socat__ thì xem phần tcp-listen sẽ cho biết port.
    * __xinetd__ thì phải xem trong file xinetd (có thể có đuôi mở rộng) tại phần port.
    * __docker-compose.yml__ thì xem phần port sẽ thấy.


## [3] Run Local use ngrok: 

- Tải ngrok về thêm key riêng của account sau đó add file ngrok vào /usr/bin để gọi như 1 command in linux.

- https://dashboard.ngrok.com/get-started/setup | VD:

```bash
ngrok tcp 1337
```
   
## [4] References:

[+] Pwn Deploy sample Dockerfile: 
- Các challenge đã làm có Dockerfile.
- [A Hiep](https://gitlab.com/hypnguyen1209/pwn-deploy).
- [A Chuoi](https://github.com/yuumi001/miniCTF2021_deploy?fbclid=IwAR19QpvrUm9jJXu_s5xvdCNkFKtN4SADFCNtQaciJWqm2cipE_LR7vRVDTQ).


[+] [USE DOCKERFILE FOR DEBUGGING WITH PWNTOOLS](https://shakuganz.com/2022/04/20/use-dockerfile-for-debugging-with-pwntools/).
