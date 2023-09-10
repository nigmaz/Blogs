# Side-Channel-Attack
- Một dạng biến thể của seccomp sandbox, gần giống với bruteforce trong CTF.
- Trong các CTF pwn challenges, side-channel attacks thường áp dụng vào việc tấn công các chương trình có lỗ hổng bảo mật. Dưới đây là một số loại side-channel attacks thường gặp:

   * `1.` **Timing Attacks**: Đây là loại tấn công sử dụng thông tin thời gian thực hiện để xác định thông tin bên trong chương trình. Ví dụ, một lỗ hổng bảo mật có thể được tiết lộ thông tin bằng cách kiểm tra thời gian thực hiện của một số phép toán.

   * `2.` **Power Analysis Attacks**: Đây là loại tấn công sử dụng thông tin về công suất tiêu tốn của một thiết bị điện tử để xác định thông tin về các hoạt động bên trong nó.

   * `3.` **Cache Attacks**: Loại tấn công này tận dụng các lỗi bảo mật trong cơ sở hạ tầng phần cứng như bộ nhớ đệm để truy cập thông tin nhạy cảm.

   * `4.` **Fault Attacks**: Loại tấn công này nhằm thay đổi trạng thái của chương trình bằng cách tạo ra các lỗi "fault" trong quá trình hoạt động.

   * `5.` **Acoustic Attacks**: Tấn công này sử dụng âm thanh được phát ra hoặc ghi âm từ thiết bị để thu thập thông tin về hoạt động bên trong.

- Trong các challenges CTF pwn, các side-channel attacks thường được sử dụng khi người thi đấu cần phá vỡ các hàm hash, mã hóa, hoặc những biện pháp bảo mật khác. Kỹ thuật side-channel cung cấp thông tin bên lề để giúp người tấn công tìm ra thông tin bí mật hoặc điều khiển luồng của chương trình.
- Tuy nhiên, để thực hiện side-channel attacks, cần phải hiểu rõ cách mà hệ thống hoạt động và cách thông tin bên lề có thể được sử dụng để tấn công.

