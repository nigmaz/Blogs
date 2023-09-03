# Github

> Git commit Github
 
- Dưới đây là tóm tắt các bước để thêm một thư mục có tên "WRITEUP" vào kho lưu trữ GitHub sử dụng Personal Access Token:

1. **Tạo Personal Access Token trên GitHub**:

   - Truy cập trang web GitHub và đăng nhập vào tài khoản của bạn (nếu bạn chưa đăng nhập).
   - Nhấn vào hình đại diện của bạn ở góc trên cùng bên phải và chọn "Settings" (Cài đặt).
   - Ở menu bên trái, chọn "Developer settings" (Cài đặt phát triển).
   - Chọn "Personal access tokens" (Token cá nhân).
   - Nhấn nút "Generate token" (Tạo token) và tuân thủ các hướng dẫn để tạo một token cá nhân. Bạn cần cấp quyền truy cập cho token này (ví dụ: repo, read:user, user:email, ...).

2. **Đặt thông tin xác thực cho tài khoản Git**:

   Mở terminal hoặc command prompt và thực hiện các lệnh sau, thay thế `"YOUR_PERSONAL_ACCESS_TOKEN"` bằng token cá nhân bạn đã tạo:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   # git credential reject
   ```

3. **Clone kho lưu trữ GitHub** (nếu bạn chưa có nó trên máy tính của mình):

   ```bash
   git clone https://github.com/nigmaz/Pwnable.git
   ```

4. **Chuyển đến thư mục đã sao chép**:

   ```bash
   cd Pwnable
   ```

5. **Tạo thư mục "WRITEUP" trong thư mục cục bộ của bạn**:

   ```bash
   mkdir WRITEUP
   ```

6. **Thêm và commit thư mục "WRITEUP" vào kho lưu trữ cục bộ**:

   - Thêm tất cả các thay đổi vào vùng chờ:

     ```bash
     git add .
     ```

   - Tiến hành commit với một thông điệp:

     ```bash
     git commit -m "Thêm thư mục WRITEUP"
     ```

7. **Đặt URL kho lưu trữ GitHub với Access Token**:

   ```bash
   git remote set-url origin https://YOUR_TOKEN@github.com/nigmaz/Pwnable.git
   ```

   Thay `YOUR_TOKEN` bằng token cá nhân bạn đã tạo.

8. **Thử lại lệnh `git push` để đẩy thay đổi lên kho lưu trữ GitHub**:

   ```bash
   git push origin main
   ```

> Lúc này, Git sẽ sử dụng token cá nhân thay vì mật khẩu để xác thực và bạn sẽ có thể đẩy thay đổi lên kho lưu trữ GitHub của bạn một cách thành công.

- Một số lệnh git thường dùng:
```bash
git config user.name
git config user.email
```
