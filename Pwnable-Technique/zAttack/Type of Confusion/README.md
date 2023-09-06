# Type of Confusion

## [0] Python pack and unpack
Trong Python, module `struct` cung cấp hai hàm quan trọng là `pack` và `unpack` để làm việc với các kiểu dữ liệu nhị phân (binary data) và các chuỗi bytes. Dưới đây là giải thích ý nghĩa của hai hàm này:

1. **Hàm `pack` trong `struct`**:

   - **Ý nghĩa**: Hàm `pack` dùng để chuyển đổi các giá trị từ các kiểu dữ liệu Python (int, float, ...) sang một chuỗi bytes theo một định dạng cụ thể. Điều này rất hữu ích khi bạn cần tạo dữ liệu nhị phân để gửi qua mạng, lưu trữ vào tệp, hoặc tương tác với các hệ thống hoạt động với dữ liệu nhị phân.

   - **Cách sử dụng**: Hàm `pack` nhận đối số đầu tiên là một chuỗi định dạng (format string) mô tả cách biểu diễn dữ liệu đầu vào, và sau đó nhận các giá trị đầu vào mà bạn muốn chuyển đổi thành chuỗi bytes.

   - **Ví dụ**: Dưới đây là một ví dụ đơn giản để chuyển đổi một số nguyên thành chuỗi bytes:

     ```python
     import struct
     
     # Chuyển đổi số nguyên 42 thành chuỗi bytes
     packed_data = struct.pack('i', 42)
     ```

2. **Hàm `unpack` trong `struct`**:

   - **Ý nghĩa**: Hàm `unpack` dùng để chuyển đổi dữ liệu từ chuỗi bytes sang các giá trị Python tương ứng với định dạng đã được xác định trước. Hàm này thường được sử dụng khi bạn muốn phân tích dữ liệu nhị phân được nhận từ mạng, đọc từ tệp, hoặc xử lý từ các nguồn dữ liệu nhị phân khác.

   - **Cách sử dụng**: Hàm `unpack` nhận đối số đầu tiên là một chuỗi định dạng (format string) mô tả cách phân tích dữ liệu từ chuỗi bytes, và sau đó nhận một chuỗi bytes chứa dữ liệu cần phân tích.

   - **Ví dụ**: Dưới đây là một ví dụ để phân tích dữ liệu từ chuỗi bytes thành số nguyên:

     ```python
     import struct
     
     # Chuỗi bytes chứa số nguyên 42
     packed_data = struct.pack('i', 42)
     
     # Phân tích chuỗi bytes để lấy giá trị
     unpacked_data = struct.unpack('i', packed_data)
     ```

Hai hàm `pack` và `unpack` trong module `struct` giúp bạn thực hiện việc chuyển đổi giữa kiểu dữ liệu Python và dữ liệu nhị phân dễ dàng và hiệu quả khi làm việc với các tình huống liên quan đến xử lý dữ liệu nhị phân.

## [1]. Argument format string in pack and unpack

Các ký tự định dạng (flags) trong chuỗi định dạng (format string) của hàm `pack` và `unpack` trong module `struct` của Python là các ký tự sử dụng để xác định kiểu dữ liệu và cách biểu diễn dữ liệu. Dưới đây là một số ký tự định dạng phổ biến:

1. **Integer Format Codes**:
   - `i`: Integer (kiểu số nguyên).
   - `I`: Unsigned integer (kiểu số nguyên không dấu).
   - `h`: Short integer (kiểu số nguyên ngắn).
   - `H`: Unsigned short integer (kiểu số nguyên ngắn không dấu).
   - `l`: Long integer (kiểu số nguyên dài).
   - `L`: Unsigned long integer (kiểu số nguyên dài không dấu).
   
2. **Floating-Point Format Codes**:
   - `f`: Float (kiểu số thực).
   - `d`: Double (kiểu số thực kép).

3. **Character Format Codes**:
   - `c`: Character (kiểu ký tự).
   - `s`: String (kiểu chuỗi ký tự, phải kèm theo kích thước).
   
4. **Byte Format Codes**:
   - `b`: Signed char (kiểu byte có dấu).
   - `B`: Unsigned char (kiểu byte không dấu).

5. **Other Format Codes**:
   - `?`: Boolean (kiểu boolean).
   - `x`: Padding byte (byte đệm).
   - `p`: Packed byte (byte được đóng gói).
   - `P`: Pointer (kiểu con trỏ).

Ký tự định dạng được sử dụng để xác định kiểu dữ liệu của giá trị và cách biểu diễn nó trong chuỗi bytes. Bạn có thể sử dụng ký tự định dạng phù hợp với kiểu dữ liệu bạn muốn định dạng và truyền dữ liệu dưới dạng chuỗi bytes giữa các ứng dụng hoặc thiết bị khác nhau.

## [3] References CTF:

- Lỗi ép kiểu là khi khai báo biến x là long (8 byte) nhưng khi xử lý điều kiện ép kiểu nó thành int (4 byte) hoặc boolean (2 byte) dẫn đến sai về mặt giá trị so sánh (trên thanh ghi).

```c
// CPP program to illustrate strstr()
#include <string.h>
#include <stdio.h>
 
int main()
{
    // Take any two strings
    char s1[] = "GeeksforGeeks";
    char s2[] = "for";
    char* p;
 
    // Find first occurrence of s2 in s1
    p = strstr(s1, s2);
 
    // Prints the result
    if (p) {
        printf("String found\n");
        printf("First occurrence of string '%s' in '%s' is '%s'", s2, s1, p);
    } else
        printf("String not found\n");
 
    return 0;
}
```

- OUTPUT:
```
String found
First occurrence of string 'for' in 'GeeksforGeeks' is 'forGeeks'
```
