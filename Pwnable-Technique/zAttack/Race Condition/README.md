# Race Condition

- Khi một chương trình `(parent process)` tạo ra các chương trình con `(more child processes)` mà các chương trình con đó truy xuất chung tới 1 biến toàn cục nào đó thì sẽ gây ra `race_condition`.
- Một số hàm tạo `child processes` từ `parent process` trong code C như: `fork()`, `pthread_create()` - lib lpthread, ...
- VD CTF: [wp racecar](https://www.youtube.com/watch?v=GxAKQuRmzMY) .

<img src="./images/race-condition.jpg" alt="Race Condition" width="500" height="300">

