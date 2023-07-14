#include <stdio.h>
#include <unistd.h>

void fun()
{
  char buf[40]; // [esp+0h] [ebp-28h] BYREF

  return read(0, buf, 0x40u);
}

int main()
{
  alarm(0xAu);
  fun();
  return 0;
}
