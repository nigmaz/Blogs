# C Sharp
> VS2019. C# settings project Type: `Console App`.

> VS2019. C++ settings project Type: `Empty project`.

### .Net (DotNet)
>[.NET](https://dotnet.microsoft.com/en-us/download)
- Là nền tảng lập trình, chạy trên Microsoft Windows.
- Không phải là ngôn ngữ lập trình, là nền tảng cho phép các ngôn ngữ khác nhau như C# sử dụng để tạo sản phẩm như viết Web.

### NOTE.

- Chương trình mẫu

```C#
using System;

namespace HelloWorld {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Hello, World!");
        }
    }
}
```

- Comment như C, Cpp.

```C#
/*Comments*/
using System;

namespace HelloWorld {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine(313 + 122); // 435
        }
    }
}

using System;

namespace HelloWorld {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("125 + 206 = " + 125 + 206);
        }
    }
}
```

- Biến được khai báo và gán giá trị như C, Cpp ; Ép kiểu `c = (long)a * b`.

```C#
using System;

namespace Variable {
    class Program {
        static void Main(string[] args) {
            // Khai báo biến c kiểu ký tự và gán giá trị cho c = ký tự 'x'
            char c = 'x';
            Console.WriteLine(c);
        }
    }
}
```

- Phương thức nhập xuất.

```C#
1) Console.Writeline("string"); // tự động thêm newline.
   Console.Write();
   
2)  string name = Console.ReadLine(); // Mặc định sẽ là nhập chuỗi nếu nhập các kiểu dữ liệu khác cần `<Kiểu dữ liệu>.Parse(Console.ReadLine())`.
    int age = int.Parse(Console.ReadLine());
    double gpa = double.Parse(Console.ReadLine());
```

- Các toán tử +, -, *, /, % giống C, Cpp.

- Câu lệnh điều kiện `if-else` giống C, Cpp.

- Vòng lặp `for, while, do-while` giống C, Cpp.

- Khai báo mảng

```C#
int[] arr = new int[10];

int[][] arr = new int[n][m];
```

- String - Phương thức.

```C#
using System;

namespace Variable {
    class Program {
        static void Main(string[] args) {
            // Khai báo biến name kiểu chuỗi các ký tự và gán giá trị cho name = "Codelearn"
            string name = "C Sharp";
            Console.WriteLine(name);
            for(int i = 0; i < name.Length; i++) {
				Console.WriteLine(name[i]);
			}
        }
    }
}
```

```C#
using System;

namespace String {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Cod3l3arn".Replace('3', 'e'));
            Console.WriteLine("Blackcat".Replace("Black", "White"));
        }
    }
}

1) ToUpper/ToLower.
2) IndexOf.
3) StartsWith, EndsWith. 
4) Split.
5) Substring.
```

- Hàm con 

```C#
using System;

namespace String {
    class Program {
        static void Main(string[] args) {
            int n = int.Parse(Console.ReadLine());
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = int.Parse(Console.ReadLine());
            }
            Console.WriteLine(SumOfArray(arr));
        }

        public static int SumOfArray(int[] arr) {
            int answer = 0;
            for(int i = 0; i < arr.Length; i++) {
                answer += arr[i];
            }
            return answer;
	    }
    }
}
```

```C#
using System;

namespace Method {
    class Program {
        public static double Circumference(double r) {
            return 2 * r * 3.14;
        }

        static void Main(string[] args) {
            double r = double.Parse(Console.ReadLine());
            Console.WriteLine(Circumference(r));
        }
    }
}
```

```C#
// Đệ quy

using System;

namespace Method {
    class Program {
        public static int Factorial(int n) {
            if(n == 1) {
                return 1;
            }
            return n * Factorial(n - 1);
        }

        static void Main(string[] args) {
            int n = int.Parse(Console.ReadLine());
            Console.WriteLine(Factorial(n));
        }
    }
}
```
