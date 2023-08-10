# Windows Service Application
## [+] Tạo một ứng dụng dịch vụ Windows bằng Visual Studio 2019 và sau đó gọi calc.exe từ trong dịch vụ này.


`Bước 1:` Tạo dự án Windows Service

- 1. Mở Visual Studio 2019.
- 2. Chọn "Create a new project".
- 3. Trong hộp thoại "Create a new project", tìm và chọn "Windows Service" dưới "Visual C#" -> "Windows".
- 4. Đặt tên cho dự án và chọn đường dẫn lưu trữ dự án của bạn.
- 5. Nhấn "Create" để tạo dự án.

`Bước 2:` Thêm mã để gọi calc.exe

- 1. Trong khung Solution Explorer, mở file Service1.cs (hoặc tên tương tự) trong thư mục Service1.
- 2. Tìm phương thức OnStart và sửa mã như sau:

```csharp
using System;
using System.ServiceProcess;
using System.Diagnostics;

namespace MyWindowsService
{
    public partial class Service1 : ServiceBase
    {
        public Service1()
        {
            InitializeComponent();
        }

        protected override void OnStart(string[] args)
        {
            // Gọi calc.exe khi dịch vụ được bắt đầu
            Process.Start("calc.exe");
        }

        protected override void OnStop()
        {
            // Không cần thực hiện gì khi dịch vụ bị dừng
        }
    }
}
```

`Bước 3:` Cấu hình dịch vụ Windows

- 1. Sau khi thêm mã vào OnStart, bạn cần cấu hình dịch vụ Windows để có thể chạy được chương trình.
- 2. Mở file Program.cs trong thư mục Service1.
- 3. Trong phương thức Main(), thay đổi dòng ServiceBase[] ServicesToRun như sau:
```csharp
ServiceBase[] ServicesToRun;
ServicesToRun = new ServiceBase[]
{
    new Service1()
};
ServiceBase.Run(ServicesToRun);
```
`Bước 4:` Xây dựng và cài đặt dịch vụ

- 1. Nhấn Ctrl + Shift + B để xây dựng dự án.
- 2. Mở Command Prompt với quyền quản trị bằng cách tìm "Command Prompt" trong menu Start, sau đó nhấn chuột phải và chọn "Run as administrator".
- 3. Di chuyển đến thư mục chứa tệp .exe đã được xây dựng, thường nằm trong thư mục bin/Debug hoặc bin/Release của dự án của bạn.
- 4. Sử dụng lệnh sau để cài đặt dịch vụ:

```powershell 
sc create MyCalcService binPath= "đường_dẫn_đến_tệp.exe"
```

- Ví dụ: sc create MyCalcService binPath= "C:\Path\To\Your\Project\bin\Debug\YourService.exe"

`Bước 5:` Khởi động và kiểm tra dịch vụ

- 1. Mở Services (dịch vụ) trên máy tính của bạn. Bạn có thể tìm thấy nó bằng cách tìm "Services" trong menu Start.
- 2. Tìm và chọn dịch vụ có tên tương ứng với tên bạn đã đặt cho dịch vụ trong bước 4.
- 3. Nhấp chuột phải và chọn "Start" để khởi động dịch vụ.
- 4. Bạn sẽ thấy calc.exe được mở.


## [+] Bạn có thể tạo một dịch vụ Windows bằng C++ để gọi calc.exe:

`Bước 1:` Tạo dự án dịch vụ Windows

- 1. Mở Visual Studio 2019.
- 2. Chọn "Create a new project".
- 3. Trong hộp thoại "Create a new project", tìm và chọn "Windows Desktop Wizard" dưới "Installed" -> "Templates" -> "Visual C++".
- 4. Chọn "Windows Service" trong danh sách các kiểu ứng dụng.
- 5. Đặt tên và vị trí cho dự án của bạn, sau đó nhấn "Create".

`Bước 2:` Thêm mã để gọi calc.exe
- 1. Mở file Service.h trong thư mục Service của dự án.
- 2. Thêm mã sau vào phần public:

```cpp
public:
    void Run();
```

- 1. Mở file Service.cpp trong thư mục Service của dự án.
- 2. Thêm mã sau vào hàm Service::Run():
```cpp
void Service::Run()
{
    // Gọi calc.exe
    system("calc.exe");
}
```
`Bước 3:` Gọi Run() từ hàm wmain

- 1. Mở file main.cpp trong thư mục Source của dự án.
- 2. Tìm hàm wmain và thay đổi mã như sau:
```cpp
int wmain(int argc, wchar_t* argv[])
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);

    Service service;
    if (!CServiceBase::Run(service))
    {
        wprintf(L"Service failed to run w/err 0x%08lx\n", GetLastError());
    }

    service.Run(); // Gọi Run() tại đây

    return 0;
}
```

`Bước 4:` Xây dựng và cài đặt dịch vụ

- 1. Nhấn Ctrl + F5 để xây dựng và chạy dịch vụ (trong chế độ gỡ lỗi).
- 2. Mở Command Prompt với quyền quản trị.
- 3. Di chuyển đến thư mục chứa tệp .exe đã được xây dựng.
- 4. Sử dụng lệnh sau để cài đặt dịch vụ:

```powershell
sc create MyCalcService binPath= "đường_dẫn_đến_tệp.exe"
```

- Ví dụ: sc create MyCalcService binPath= "C:\Path\To\Your\Project\Debug\YourService.exe"

`Bước 5:` Khởi động và kiểm tra dịch vụ

- 1. Mở Services (dịch vụ) trên máy tính của bạn.
- 2. Tìm và chọn dịch vụ có tên tương ứng với tên bạn đã đặt cho dịch vụ trong bước 4.
- 3. Nhấp chuột phải và chọn "Start" để khởi động dịch vụ.
- 4. Bạn sẽ thấy calc.exe được mở.
