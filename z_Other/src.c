#include<stdio.h>
#include<stdlib.h>

struct Bill
{
  Bill *nextBill;
  user *sr_USER;       // user send or recv
  int TransID;
  int type;         // 1 is type bill recv and 0 is type bill send
  int coin;
};

struct user
{
  char *name;
  char *pass;
  int money;
  Bill *Trans;
};

void *userList;
int countTrans;

int title()
{
  putchar(10);
  puts(" _______ _______ _______ __   __ _______ _______ ___ __    _ ");
  puts("|       |   _   |       |  | |  |       |       |   |  |  | |");
  puts("|    ___|  |_|  |  _____|  |_|  |       |   _   |   |   |_| |");
  puts("|   |___|       | |_____|       |       |  | |  |   |       |");
  puts("|    ___|       |_____  |_     _|      _|  |_|  |   |  _    |");
  puts("|   |___|   _   |_____| | |   | |     |_|       |   | | |   |");
  puts("|_______|__| |__|_______| |___| |_______|_______|___|_|  |__|");
  putchar(10);
  return puts("Welcome to EasyCoin. This is a one of easiest crypto-currency. At first, please register user.");
}

unsigned int setup()
{
  unsigned int result; // eax
  int i; // [rsp+Ch] [rbp-4h]

  setvbuf(stdout, 0LL, 2, 0LL);
  setvbuf(stdin, 0LL, 1, 0LL);
  result = alarm(0);
  for ( i = 0; i <= 4; ++i )
    ;
  return result;
}

char readStr(char *a1, int a2){
    char *result;
    int i;

    read(0, a1, a2);
    for(i = strlen(a1) - 1; i>= 0; --i){
        if(a1[i] == 10){
            a1[i] = 0;
            return 0;
        }
    }
    result = &a1[strlen(a1)];
    *result = 0;
    return result;
}

int login(){
    int i;
    char s2[40];

    printf("Please input username\n> ");
    readStr(s2, 31);
    for(i = 0; ; ++i){
        if(i > 4){
            puts("[-] This user is not registered");
            return 0;
        }
        if(*(&userList + i) && !strcmp(*(const char **)*(&ptr + i), s2))
            break;
    }
    printf("Please input password\n> ");
    readStr(s2, 31);
    if(!strcmp(*(const char **)*((&ptr + i) + 1), s2))
        return (__int64)*(&userList + i);
    puts("[-] Password error");
    return 0LL;
}

int register(){
  void **v1; // rbx
  __int64 v2; // rbx
  int id; // [rsp+4h] [rbp-4Ch]
  int i; // [rsp+8h] [rbp-48h]
  int j; // [rsp+Ch] [rbp-44h]
  char s2[40]; // [rsp+10h] [rbp-40h] BYREF
  unsigned __int64 v7; // [rsp+38h] [rbp-18h]

  v7 = __readfsqword(0x28u);
  id = -1;
  printf("Please input username\n> ");
  readStr_400A1A(s2, 31);
  for ( i = 0; i <= 4; ++i )
  {
    if ( *(&ptr + i) && !strcmp(*(const char **)*(&ptr + i), s2) )
    {
      puts("[-] This user already registerd");
      return 1LL;
    }
  }
  for ( j = 0; j <= 4; ++j )
  {
    if ( !*(&ptr + j) )
    {
      id = j;
      break;
    }
  }
  if ( id == -1 )
  {
    puts("[-] User Registration is over");
    exit(0);
  }
  *(&ptr + id) = malloc(0x20uLL);
  v1 = (void **)*(&ptr + id);
  *v1 = malloc(0x20uLL);
  v2 = (__int64)*(&ptr + id);
  *(_QWORD *)(v2 + 8) = malloc(0x20uLL);
  *((_QWORD *)*(&ptr + id) + 2) = 1000000000LL; // coin
  *((_QWORD *)*(&ptr + id) + 3) = 0LL;
  strncpy(*(char **)*(&ptr + id), s2, 0x1FuLL);
  printf("Please input password\n> ");
  readStr_400A1A(*((char **)*(&ptr + id) + 1), 31);
  printf("Verify input password\n> ");
  readStr_400A1A(s2, 31);
  if ( !strcmp(*((const char **)*(&ptr + id) + 1), s2) )
  {
    puts("[+] Registration success");
  }
  else
  {
    puts("[-] Password confirmation failed");
    free(*(void **)*(&ptr + id));
    free(*((void **)*(&ptr + id) + 1));
    free(*(&ptr + id));
    *(&ptr + id) = 0LL;
  }
  return 0LL;
}

int main(__int64 a1, char **a2, char **a3)
{
  int choice; // eax
  int checkLogin; // [rsp+Ch] [rbp-24h]
  const user *username; // [rsp+18h] [rbp-18h]
  char buf[8]; // [rsp+20h] [rbp-10h] BYREF

  setup();
  title();
  checkLogin = 0;
  username = 0;
  while ( 1 )
  {
    puts("------------------------------------------------");
    puts(" 1: register user");
    puts(" 2: login user");
    puts(" 3: exit");
    puts("------------------------------------------------");
    puts("which command?");
    printf("> ");
    read(0, buf, 4);
    choice = atoi(buf);
    switch ( choice )
    {
      case 2:
        username = (void **) login();     
        // return (__int64)*(&ptr + i);
        if ( username )
        {
          printf("[+] Welcome to EasyCoin, %s\n\n", username->name);
          checkLogin = 1;
        }
        break;
      case 3:
        exit(0);
      case 1:
        register();
        break;
      default:
        puts("[-] Invalid command!");
        break;
    }
    // while ( checkLogin )
    // {
    //   puts("------------------------------------------------");
    //   puts(" 1: display user info");
    //   puts(" 2: send coin");
    //   puts(" 3: display transaction");
    //   puts(" 4: change password");
    //   puts(" 5: delete this user");
    //   puts(" 6: logout");
    //   puts("------------------------------------------------");
    //   puts("which command?");
    //   printf("> ");
    //   read(0, buf, 4uLL);
    //   switch ( buf[0] )
    //   {
    //     case '1':
    //       display_400EAE((__int64)username);
    //       break;
    //     case '2':
    //       send_400FAB((__int64)username);
    //       break;
    //     case '3':
    //       viewTrans_400EE2(username);
    //       break;
    //     case '4':
    //       changePass_401372(username);
    //       break;
    //     case '5':
    //       sub_4013C8(username);
    //       checkLogin = 0;
    //       break;
    //     case '6':
    //       checkLogin = 0;
    //       break;
    //     default:
    //       printf("[-] Unknown Command: ");
    //       printf(buf);
    //       break;
    //   }
    // }
  }
}


// struct user
// {
//   char *name;
//   char *pass;
//   __int64 money;
//   Bill *Trans;
// };

// struct Bill
// {
//   Bill *nextBill;
//   user *srUSER;
//   __int64 TransID;
//   __int64 type;
//   __int64 amount;
// };