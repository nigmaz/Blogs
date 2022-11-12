# Script for Docker

>NOTE: Cheatsheet command line .

Docker là một platform cung cấp cho người dùng những công cụ và service để có thể building, deploying và running ứng dụng dễ dàng hơn bằng cách sử dụng các containers (trên nền tảng ảo hóa).

```
[DOCKER FILE] ==|build|==> [Image] ==|run|==> [Containers]  
```

  - `Docker Registry` : Nơi chứa Docker Image.
  
  - `Docker Compose` : là công cụ cho phép bạn chạy Ứng Dụng với nhiều Docker Containers một cách nhanh chóng và dễ dàng.

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

### 3) Run Local use Ngrok: 

   * [Video](https://www.youtube.com/watch?v=jOm_XSeMnJI&t=33s) .
   
   * [Video](https://www.youtube.com/watch?v=9BJmDa0TIgw) .

   * [Tutorial](https://viblo.asia/p/tooling-gioi-thieu-ngrok-mang-demo-du-an-web-len-internet-khong-can-deploy-naQZR7eqlvx) .
   
   * Pwn Deploy sample: [A Hiep](https://gitlab.com/hypnguyen1209/pwn-deploy), [A Chuoi](https://github.com/yuumi001/miniCTF2021_deploy?fbclid=IwAR19QpvrUm9jJXu_s5xvdCNkFKtN4SADFCNtQaciJWqm2cipE_LR7vRVDTQ) .
-------------------------------------------------------------------------------------------------------

### REF:

[+] [Docker](https://gist.github.com/chaseYLC/3d2ab4c6955044f21da628546c0c6977) .

