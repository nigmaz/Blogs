# Kernel Source setup

- Edit /root/.gdbinit => debug sudo gdb | plugin gdb
```bash
source /home/nigmaz/Public/.gdbinit-gef.py
add-auto-load-safe-path /home/nigmaz/.gdbinit
set auto-load safe-path /
```

- Build minimal-kernel | https://gist.github.com/chrisdone/02e165a0004be33734ac2334f215380e
