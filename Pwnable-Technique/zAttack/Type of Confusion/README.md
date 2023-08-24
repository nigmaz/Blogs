# Type of Confusion

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
