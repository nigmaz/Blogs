# Script for Docker

>NOTE: Cheatsheet command line .

>link:

  * https://wyv3rn.tistory.com/165
  
  * https://wyv3rn.tistory.com/233

Docker là một platform cung cấp cho người dùng những công cụ và service để có thể building, deploying và running ứng dụng dễ dàng hơn bằng cách sử dụng các containers (trên nền tảng ảo hóa).

```
[DOCKER FILE] ==|build|==> [Image] ==|run|==> [Containers]  
```

  - `Docker Registry` : Nơi chứa Docker Image.
  
  - `Docker Compose` : là công cụ cho phép bạn chạy Ứng Dụng với nhiều Docker Containers một cách nhanh chóng và dễ dàng.
  
  - sudo service docker status

## Các câu lệnh thường dùng.

### 1) Build Image:

```
$
docker build -t <name_image> . 
[NOTE là có dấu "."]
$
docker images -a 
[Liệt kê các image và lấy ID image].
```

### 2) Run Image:

```
$ 
docker run -d -p <port>:<port> --rm -it <name/ID image>

NOTE:
-d : là chạy nền .
-p : chứa đến một cổng trên máy chủ của tôi .
--rm : tự động xóa vùng chứa khi thoát vùng chứa .

$ 
docker ps -a 
[Liệt kê các containers đang chạy]

$
docker exec -it <ID CONTAINERS STATUS> /bin/bash
[Thực thi câu lệnh yêu cầu]

$
docker stop <name containers (h) ID containers>

$
docker rmi <name (h) ID images>
[xóa Image].

docker rm <container name>
[xóa Container].
```

STOP ALL

```
$ Stop all running containers.
docker stop $(docker ps -a -q)

$ Delete all stopted containers.
docker rm $(docker ps -a -q)

$ Delete all image.
docker rmi $(docker images -q)

$ Xóa tất cả image và tài nguyên không sử dụng.
docker system prune

```

```
Một số vị trí nhận biết port
socat thì xem phần tcp-listen sẽ cho biết port
xinetd thì phải xem trong file xinetd (có thể có đuôi mở rộng) tại phần port
docker-compose.yml thì xem phần port sẽ thấy

Một số lệnh docker thường
* Build và run:
sudo docker build . -t "tag-name"
sudo docker run --rm -p "host-port":"docker-port" -it "tag-name"
sudo docker run --rm -p "host-port":"docker-port" --privileged -it "tag-name"
sudo docker-compose up --build

* Liệt kê các container đang chạy:
sudo docker ps

* Thực thi lệnh linux trong docker:
sudo docker exec -it "containter-id" "commands"
sudo docker-compose exec "service-name" "commands"

* Lấy file từ docker ra host:
sudo docker cp "container-id":"path-to-file-in-docker" "path-to-file-in-host"

Đối với wsl, để chạy được lệnh docker cần chạy nền docker daemon với lệnh sau: sudo dockerd &
```

### 3) Run Local use Ngrok: 

   * [Video](https://www.youtube.com/watch?v=jOm_XSeMnJI&t=33s) .
   
   * [Video](https://www.youtube.com/watch?v=9BJmDa0TIgw) .
   
   * [Video](https://www.youtube.com/watch?v=uG1QW5UWVrU) .

   * [Tutorial](https://viblo.asia/p/tooling-gioi-thieu-ngrok-mang-demo-du-an-web-len-internet-khong-can-deploy-naQZR7eqlvx) .
   
   * Pwn Deploy sample: [A Hiep](https://gitlab.com/hypnguyen1209/pwn-deploy), [A Chuoi](https://github.com/yuumi001/miniCTF2021_deploy?fbclid=IwAR19QpvrUm9jJXu_s5xvdCNkFKtN4SADFCNtQaciJWqm2cipE_LR7vRVDTQ) .
-------------------------------------------------------------------------------------------------------

### REF:

[+] [Docker](https://gist.github.com/chaseYLC/3d2ab4c6955044f21da628546c0c6977) .

[+] [USE DOCKERFILE FOR DEBUGGING WITH PWNTOOLS](https://shakuganz.com/2022/04/20/use-dockerfile-for-debugging-with-pwntools/) .

[+] [Search `setup docker local for debug pwn ctf`] .



