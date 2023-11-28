# WindowsAPI - MFC Application

> WindowsAPI and MFC Application (language C or Cpp).

## [0]. NOTE:

- `Config`:
  - [Deploy a Visual C++ application](https://learn.microsoft.com/en-us/cpp/windows/walkthrough-deploying-a-visual-cpp-application-by-using-a-setup-project?view=msvc-170).
  - Project type: `Empty Project`.

  - Config project: Properties > Linker > System > `SubSystem : Windows (/SUBSYSTEM:WINDOWS)`.

  - Project multi-byte: Properties > Advanced (or. General for older versions) > Character Set, option to `Use Multi-Byte Character Set`.
  - ...

- `Error`:
  - Fix error chinese language display in visual studio: [add utf-8 into Character Set](https://learn.microsoft.com/en-us/cpp/build/reference/utf-8-set-source-and-executable-character-sets-to-utf-8?view=msvc-170#set-the-option-in-visual-studio-or-programmatically) .
    - Open the project Property Pages dialog box.
    - Configuration Properties > C/C++ > Command Line > Additional Options, add the `/utf-8` (or `/utf-16`).

  - ...
 
- `Run and Debug`:
  - Debug with arguments: Configuration Properties > Debugging > Command Arguments, add the argv[] `...`.
  - ...

## [1]. Knowledge:

- Khác biệt chính giữa cấu hình SubSystem "Windows" (/SUBSYSTEM:WINDOWS) và "Console" (/SUBSYSTEM:CONSOLE) nằm ở cách mà chương trình của bạn sẽ chạy và tương tác với môi trường hệ thống:

  - 1. **SubSystem: Windows (/SUBSYSTEM:WINDOWS):** Khi chọn cấu hình này, chương trình của bạn sẽ không hiển thị cửa sổ dòng lệnh (command prompt) khi chạy. Thay vào đó, nó sẽ chạy trong môi trường giao diện người dùng Windows (GUI). Đây là cấu hình thích hợp cho các ứng dụng desktop hoặc ứng dụng không cần giao diện dòng lệnh.
  ```cpp
  int WINAPI WinMain(
  HINSTANCE hInstance,
  HINSTANCE hPrevInstance,
  LPSTR lpCmdLine,
  int nCmdShow
  ) {
    ...
    return 0;
  }
  ```
  - 2. **SubSystem: Console (/SUBSYSTEM:CONSOLE):** Khi chọn cấu hình này, chương trình của bạn sẽ chạy trong cửa sổ dòng lệnh (command prompt). Điều này cho phép chương trình xuất thông tin ra dòng lệnh và tương tác với người dùng thông qua giao diện dòng lệnh. Đây thường là cấu hình được chọn cho các ứng dụng cần tương tác người dùng hoặc cần xuất thông tin ra dòng lệnh.
  ```cpp
  int wmain(int argc, wchar_t* argv[])
  {
    ...
    return 0;
  }
  ```
  - Lựa chọn giữa "Windows" và "Console" phụ thuộc vào loại ứng dụng mà bạn định xây dựng. Nếu bạn định xây dựng một ứng dụng với giao diện người dùng hoặc một dịch vụ Windows, bạn có thể chọn SubSystem là "Windows". Nếu bạn muốn chương trình của mình tương tác với người dùng thông qua dòng lệnh, bạn sẽ chọn SubSystem là "Console".

- Trong lập trình Windows, `HINSTANCE` là một kiểu dữ liệu thường được sử dụng để đại diện cho một thể hiện (instance) của một ứng dụng Windows. Kiểu dữ liệu này thường là một con trỏ hoặc một loại cấu trúc có thể chứa thông tin về việc thực thi của chương trình.

  - Đối với hàm `WinMain` hoặc các hàm tương tự trong lập trình Windows, `HINSTANCE` được sử dụng để đại diện cho thể hiện của chính chương trình đang chạy. Điều này có thể được sử dụng để truy cập các tài nguyên như biểu tượng, dữ liệu tệp tin, hay các cấu trúc dữ liệu khác mà chương trình cần để hoạt động.

  - Ví dụ, `HINSTANCE` có thể được sử dụng để:

    - Load tệp tin resource như hình ảnh, âm thanh, hoặc cấu trúc dữ liệu từ tệp tin resource của chương trình.
    - Tạo ra cửa sổ windows, điều này thường yêu cầu thông tin từ thể hiện của ứng dụng.
    - Truy cập thông tin về đường dẫn của chương trình, ví dụ như để mở các tệp tin nằm trong cùng thư mục với chương trình.

  - `HINSTANCE` thường được truyền vào các hàm Windows như là một tham số để cho phép chương trình truy cập thông tin về thể hiện của chính nó và thực hiện các tác vụ liên quan đến việc quản lý tài nguyên và giao diện.

- ...

## [2] References:

[+] learn Win32 - [Document](http://www.winprog.org/tutorial/start.html) .

[+] code WinAPI + ASM [Ref](https://www.youtube.com/watch?v=pdgmlto7Uwc) .

[+] [Video Tutorial](https://www.youtube.com/watch?v=yvWYggka30A) .

[+] [List video WinAPI - MFC Programming](https://www.youtube.com/watch?v=60O6B2Di5RE&list=PLfszubEEhakf7mGTDjsImyp-YGU69_S5k&index=42) .

[+] Learn: `learn mfc` - https://functionx.com/visualc/index.htm .

[+] WIN32 API:
- https://learn.microsoft.com/en-us/cpp/windows/overview-of-windows-programming-in-cpp?view=msvc-170
- `dll`: https://learn.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-dynamic-link-library-cpp?view=msvc-170
- [youtube Windows System Programming in C/C++](https://www.youtube.com/watch?v=B999K9yztnI&list=PLDpFwQfbVxIw_rysNCHPeGmh6wIUnhjrt)
- https://learn.microsoft.com/en-us/windows/win32/api/


1. **ASCII (American Standard Code for Information Interchange)**:
   - ASCII là một bộ mã ký tự tiêu chuẩn được phát triển trong những năm 1960 tại Hoa Kỳ.
   - Nó chỉ sử dụng 7 bit để biểu diễn ký tự (từ 0 đến 127).
   - ASCII chỉ hỗ trợ các ký tự tiếng Anh cơ bản, số, dấu câu và các ký tự đặc biệt. Nó không hỗ trợ các ký tự đặc biệt của các ngôn ngữ khác.
   - Ví dụ: 'A', 'B', '1', '$', '@'.

2. **UTF-8 (Unicode Transformation Format - 8 bits)**:
   - UTF-8 là một bộ mã ký tự Unicode tiêu chuẩn.
   - Nó sử dụng từ 1 đến 4 byte để biểu diễn một ký tự. Điều này cho phép nó hỗ trợ hầu hết các ngôn ngữ và biểu tượng trên thế giới.
   - Ký tự ASCII sẽ có cùng mã trong UTF-8 (nghĩa là, ký tự ASCII sẽ vẫn được biểu diễn bởi một byte như cách nó được biểu diễn trong ASCII).
   - UTF-8 cũng có thể biểu diễn ký tự từ nhiều vùng Unicode khác nhau.
   - Ví dụ: 'A', 'B', '1', '$', '@', các ký tự tiếng Trung, tiếng Nhật, tiếng Ả Rập, vv.

Trong tổng quát, UTF-8 được coi là một bộ mã ký tự mở rộng vượt xa khỏi phạm vi của ASCII và là một tiêu chuẩn rất phổ biến cho biểu diễn các ký tự trong các ứng dụng hiện đại.




      

      
