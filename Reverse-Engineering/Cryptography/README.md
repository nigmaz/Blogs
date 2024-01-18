# Cryptography

- Crypto (Dreamhack)
- https://cryptohack.org/courses/
- https://cryptopals.com/
- `Tools`: https://gchq.github.io/CyberChef/, kt.gy,...
- Các loại mã hóa thường gặp khi Reverse:
  - RC4
  - XOR (XOR với 1 ký tự hoặc là XOR với 1 chuỗi byte, chuỗi ký tự)
  - AES mode ECB
  - RSA
  - Base64
  - 

## [0]. RC4

> Mã hóa đối xứng.

- KSA | PGSA (hoặc gọi là PRG) sinh ra bảng mã s-box, sau đó dùng thuật toán để tìm idx trong s-box rồi dùng ký tự s-box để xor tạo encrypt-text.
- `Plaintext` XOR `STREAMKEY` => `Ciphertext`.
- Trong đó quá trình tạo `STREAMKEY` từ `SECRETKEY` được cho là ngẫu nhiên và không thể đảo ngược do vị trí các giá trị % 256 ra idx trong S-box là rất nhiều.
- VD `secretkey` => `streamkey`:

  - Stage-1: Chuẩn bị key - KSA:
    - Input của khâu này là key bí mật của chúng ta [3, 1, 0, 0]
	  - Output của khâu này là một hoán vị của dạy S = [0, 1, 2, 3, 4, 5, 6, 7]
	  - (Trên thực tế, dãy S là từ 0 đến 255 để tương thích với hệ ASCII, nhưng ở đây ta chỉ lấy là 8 cho đơn giản).
  ```python
  S[256] = {}
  for i from 0 to 256:
    S[i] = i
  j = 0
  for i from 0 to 256:
	  j = (j + S[i] + key[i % length(key)]) % 256
	  swap values of S[i] and S[j]
  ```

  - Stage-2: Thuật toán sinh giả ngẫu nhiên - PRNG
    - Thuật toán trên sẽ sinh ra output giả ngẫu nhiên tùy vào độ dài của plaintext.
    - Thuật toán trên sẽ sinh ra output giả ngẫu nhiên dài tùy thích, tùy vào độ dài plaintext. Ví dụ:
    - 1) plaintext = [1, 2, 3], output sẽ chỉ sinh ra đến [1, 4, 1], từ đó cho ciphertext = [1, 2, 3] xor [1, 4, 1] = [0, 6, 2]
    - 2) plaintext = [5, 6, 7, 6, 5, 4, 3, 2, 1], output sẽ sinh ra đến [1, 4, 1, 5, 7, 7, 7, 0, 5], từ đó cho ciphertext = [4, 2, 6, 3, 2, 3, 4, 2, 4]
  ```python
  i = 0
  j = 0
  while output_length < plaintext_length:
  	i = (i + 1) % 256
  	j = (j + S[i]) % 256
  	swap values of S[i] and S[j]
  	output K = S[(S[i] + S[j]) % 256]
  ```

## [1]. Base64



- 3 byte (24 bit) chia thành 4 character (24 / 6 | mỗi char nhận 6 bit), nếu thiếu thì padding sử dụng dâu `=`.


## [2]. ...
  
