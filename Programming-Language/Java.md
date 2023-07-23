# JAVA
> Java Virtual Machine, Java Development Kit, Java Runtime Environment.
- Install [Java JDK](https://www.oracle.com/java/technologies/downloads/) .
```c
java -version   // this will check your jre version
javac -version  // this will check your java compiler version if you installed
```

## [0]. IDE.
> Use `Eclipse` to code Java. 
- [Java Tutorial New Project Eclipse](https://www.youtube.com/watch?v=uksb46znL58). 

> Use `NetBeans` to code Java.
- [Java Tutorial New Project NetBeans](https://www3.ntu.edu.sg/home/ehchua/programming/howto/netbeans_howto.html). 

- Java video learn:
  * [Cô Vân Anh](https://www.youtube.com/watch?v=9dddxv8E5Mk&list=PLD8zSU7U1L2HjyE8U_ojnYOe1_zixZjsc) .
  * [Java + CNPM](https://www.youtube.com/watch?v=c4q7n5cmEOM&list=PL43ofROd3vU8aGy5hId6RM4YT8Nr8N2e7) .
  * [BTL+project Java](https://www.youtube.com/watch?v=WKL0jsNrFzY&list=PL8JRkLx_73-KoDilxKX-DT5it1xlhj5f-) .
  * https://youtu.be/w3QmdZSshag
  * https://youtu.be/0PPzWgRxpFk

- Code Android: android studio app

## [1]. NOTE:
- In ra màn hình.

```java
System.out.print("Hello Java!!!"); // In không xuống dòng.
System.out.println("Hello Java!!!"); // Tự động newline khi in xong.
```
VD:

```java
System.out.print("125 + 206 = " + (125+206)); // 125 + 206 = 331.
```

- Comments code giống C, Cpp, C#.
- Khai báo biến giống C, Cpp.
- Ép kiểu dữ liệu. `c = (long)a + b`.
- Nhập xuất.

- Yêu cầu: 
  * `import java.util.Scanner;`.

  * `Scanner sc = new Scanner(System.in);` | gán phương thức nhập Scanner = sc .

- [Nhập xuất](https://loda.me/articles/jav4-nhap-xuat-du-lieu-trong-java) .

VD:

```java
String name = sc.next();
String tenChuoi = "giá_trị_khởi_tạo";
int age = sc.nextInt();
double gpa = sc.nextDouble();
```

- Lớp `Scanner` không cung cấp phương thức để nhập dữ liệu kiểu char, thay vào đó cần nhập dữ liệu kiểu `String` và lấy ra ký tự đầu tiên trong String.

```java
char c = sc.next().charAt(0);
```

- Cấu trúc `if else` giống C, Cpp.
- Vòng lặp giống C, Cpp.
- Mảng(Array).

```java
// Mảng một chiều.
int[] a = new int[10];
for(int i = 0; i < 10; i++){
  a[i] = sc.nextInt();
}
// Mảng hai chiều.
int[][] arr = new int[n][m];
```

- Xâu(String).

```java
s.charAt(0);
s.charAt(1);
s.charAt(2);
s.charAt(3);
```

- Phương thức: Một số phương thức như (Hàm con).

```java
1) s.length();
2) s.charAt(i);
3) s.replace('3', 'e');
4) s.toUpperCase();
   s.toLowerCase();
5) s.indexOf("learn");
6) s.startsWith(" ");
   s.endsWith(" ");
7) s.split(" ");
8) s.substring(0, 2);
```

- Truyền đối số như C, Cpp.

```java
public class <name>{
  public static int <name>(int ...){
    ...
  }
  public static void main(String[] args){
    ...
  }
}
```

