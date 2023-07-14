# PYTHON
> [Install Python3 Windows](https://www.python.org/downloads/) and [get-pip.py](https://bootstrap.pypa.io/get-pip.py).

## [0]. IDE.
- Pycharm - [Configure a Python interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html) .

- [Python environment project LINUX](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-20-04-quickstart) .

>Python Project Example:

	- [Flappy Bird](https://www.youtube.com/watch?v=MMxFDaIOHsE) .
	
	- [Object Tracking](https://www.youtube.com/shorts/ocA30qI9Z-M) .

## [1]. NOTE:
- Các kiểu dữ liệu trong python.

1) Numbers: int, long, float, complex(số phức), ...

2) String: Dùng (*) (lặp chuỗi) ; Dùng (+) (nối chuỗi).

3) List[,,]: Dãy bao gồm có thể là cả sỗ lẫn chuỗi ; Có thể đặt lại giá trị của các phần tử ; [ : ].

4) Tuple(,,): Tương đối giống List, khác là không thể đặt lại giá trị. -> chỉ đọc.

5) Dictionary{,,}: cặp keys - values

list, tuple, arr (numpy, array [chuyên đặc tả dữ liệu]), set, directory 

list - set [set không lưu giá trị trùng] | map - direct [direct là kiểu dữ liệu mà các key không được lặp lại]

>Không cần khai báo kiểu dữ liệu. Muốn biết kiểu dữ liệu gì print(type(<var>)).

> Hàm round(number, ndigits) | ndigits là số chữ số cần làm tròn.
	
>Muốn biết một hàm dùng để làm gì trong python shell sử dụng `help(tên hàm)`.
	
```python
>>> help(pow)
Help on built-in function pow in module builtins:

pow(base, exp, mod=None)
Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

Some types, such as ints, are able to use a more efficient algorithm when
invoked using the three argument form.
```
	
- Nhập xuất.
  
```python
name = input()
print("Hello " + name)
```

>Khi nhập dữ liệu cho một biến từ keyboard thì kiểu dữ liệu đó luôn là str (kể cả nhập gái trị số cho biến đó). Muốn thay đổi kiểu dữ liệu thì phải ép kiểu.
  
```python
a = int(input())
b = float(input())
```
  
- Toán tử không có gì khác các ngôn ngữ khác. Thêm `**` là tính lũy thừa a**b = a mũ b, `//` là chia lấy phần nguyên. 

  VD: 2**3 = 8 ; 9 // 2 = 4.
  
  Toán tử membership để kiểm tra xem 1 giá trị có nằm trong giá trị khác không. `in` và `not in`.
  
  VD: x = input()
      print('H' in x)
  
  Toán tử định danh
  
  VD: a = int(input())
      b = int(input())
      print(a is b)
  
  Toán tử logic giống C, Cpp.
  
- Điều kiện `if-else`.
  
```python
if a == b:
	print("a == b")
else:
	if a > b:
		print("a > b")
	else:
		print("a < b")

# Hoặc là.
if a == b:
	print("a == b")
elif a > b:
	print("a > b")
else:
	print("a < b")			
```

- Vòng lặp.
		
```python
	while i <= 5:
		print(i)
		i += 1
		
	for i ỉn range(1, 5):
		print(i)
	
	c = "Hello Python"
	for c in name:
		print(c)
```

- Mảng

Tạo ra list để lưu trữ các số nguyên
		
```python
# Tạo ra list để lưu trữ các số nguyên
list1 = [1, 2, 3]
# Tạo ra list để lưu trữ các xâu ký tự
list2 = ["Viet", "Tuan", "Duong"]
# Bạn cũng có thể tạo ra một list lưu trữ các kiểu dữ liệu khác nhau
list3 = [7, 3.5, "Codelearn"]
print(list1[0])
print(list1[1])
print(list1[2])
		
# Nhập phần tử.
lst = []
lst.append(4)
lst.append(3)
lst.append(6)
print(lst)
		
# Các hàm hay dùng.
len(lst) # trả về số phần tử của list
max(lst) # trả về phần tử lớn nhất
min(lst) # trả về phần tử nhỏ nhất
		
vowels = ['a', 'e', 'i', 'u']
# Chèn xâu 'o' vào vị trí thứ 4 trong list vowels
vowels.insert(3, 'o')
print(vowels)
# Output: ['a', 'e', 'i', 'o', 'u']

lst = ['A', 'B', 'C']
lst.remove('A')
print(lst)
# Output: ['B', 'C']
		
# Xóa phần tử với chỉ số cho trước
lst = ['A', 'B', 'C']
# Xóa phần tử thứ 2 khỏi list
lst.pop(1)
print(lst)		
# Output: ['A', 'C']
		
lst.sort() # sắp xếp tăng dần
lst.sort(reverse=True) # sắp xếp giảm dần
lst.reverse() # Đảo ngược chuỗi

# Đếm số lần xuất hiện của phần tử cho trước 
lst = [6, 2, 3, 8, 2]
print(lst.count(2))
# Output: 2

lst.clear() # xóa hết phần tử trong list.
```
  
- Chuỗi

```python
a = "abc123"
s = """
Banana
Apple
Orange
"""
print(s)
		
len(s)
s.lower()
s.upper()
# Kết quả sẽ là False nếu chuỗi s có ký tự khác ngoài ký tự chữ và số.
print(s.isalnum())
# Kết quả sẽ là False do chuỗi s chứa số.
print(s.isalpha())
# Kiểm tra xem có phải là số hay không.
s = "2020"
print(s.isnumeric())
		
s = "Welcome to Python"
print(s.split(" "))
# ['Welcome', 'to', 'Python']
		
lst = ["A", "B", "C"]
print("-".join(lst))
# A-B-C
		
name = "Cod3l3arn"
print(name.replace("3", "e"))
# Codelearn
```
  
Cắt chuỗi
		
```python
s = 'Python String'
print(s[0:2])
print(s[3:5])
print(s[7:])
print(s[:6])
print(s[7:-4])

'''
Py
ho
String
Python
St
'''
```

- Hàm con.

```python
# def <name>(<arguments>):
# không return nghĩa là như hàm void.

def show(s):
    count_upper = 0
    count_lower = 0
    for c in s:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1

    print("Given string:", s)
    print("Number of uppercase letters:", count_upper)
    print("Number of lowercase letters:", count_lower)
		
def get_unique_values(lst):
    answer = []
    for v in lst:
        if v not in answer:
            answer.append(v)
    return answer
```

>Note: Python3. VD: b'<string>'. u là chuỗi unicode ; b là biểu thị chuỗi kí tự byte ; r là chuỗi kí tự không thoát ra được @@. Không có `,` và `;`.
