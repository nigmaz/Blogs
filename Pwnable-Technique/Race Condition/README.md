# Race Condition

- Khi một chương trình `(parent process)` tạo ra các chương trình con `(more child processes)` mà các chương trình con đó truy xuất chung tới 1 biến toàn cục nào đó thì sẽ gây ra `race_condition`.
- Một số hàm tạo `child processes` từ `parent process` trong code C như: `fork()`, `pthread_create()`, ...

<img src="./images/race-conditions.jpg" alt="Race Conditions" width="500" height="300">

[+] VD CTF: [wp racecar](https://www.youtube.com/watch?v=GxAKQuRmzMY) .
