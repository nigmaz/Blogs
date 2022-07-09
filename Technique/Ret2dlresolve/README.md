# Ret2dlresolve 
>Trả về hàm `_dl_runtime_resolve` với các tham số được tùy chỉnh nhằm giải quyết bất kì hàm nào trong libc mà chúng ta muốn gọi. 

Tổng hợp ngắn gọn lại các cấu trúc và thuật toán cần fake để thực hiện `ret2dlresolve`, để nắm vững kĩ thuật nên làm ví dụ mẫu, đọc writeup. Tôi sẽ đi từ kiến trúc `32 bit` trước vì nó đơn giản hơn khi khai thác trên kiến trúc này. Trên kiến trúc `64 bit` về cơ bản cấu trúc không thay đổi nhiều, có thay đổi về vị trí, một vài dữ liệu trong cấu trúc, thuật toán kiểm tra dữ liệu. Tôi sẽ viết kỹ hơn khi đề cập đến đó  

## 1) 32 bit.
> Tôi sử dụng kỹ thuật này khi file là 32 bit, ASLR, NX, Partial RELRO, NO PIE và không có Canary. Không xác định được phiên bản `libc` và không có cách nào để `leak` được dữ liệu.

## 2) 64 bit.

-----------------------------------------

[+]

[+]

[+]

