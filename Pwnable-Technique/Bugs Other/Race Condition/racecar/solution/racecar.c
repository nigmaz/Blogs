#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

pthread_t thread_id[10];
char *racers[10];
unsigned int racer_num = 0;

void init()
{
	int fd, seed;

	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	fd = open("/dev/urandom", 0, 0);
	read(fd, &seed, 4);
	srand(seed);
	close(fd);
}

void remove_newline()
{
	while(getchar() != '\n');
}

void get_flag()
{
	system("cat flag.txt");
}

void menu()
{
	puts("-------------- RACERS --------------");
	for (unsigned int i=0 ; i<racer_num; i++)
		printf("Racer %u: %s\n", i+1, racers[i]);
	puts("------------------------------------");
	puts("1. Add racer");
	puts("2. Race");
	puts("3. Exit");
	printf("> ");
}

void *race(void *args[])
{
	char *racer_name = args[0];
	char *winner = args[1];
	usleep(rand() % 1000);
	usleep(rand() % 1000);
	usleep(rand() % 1000);
	if (*winner == '\0')
		strcat(winner, racer_name);
}

void run()
{
	int option, done = 0;
	char winner[256];
	void *args[10][2];
	memset(winner, 0, sizeof(winner));

	while (!done)
	{
		menu();
		scanf("%d", &option);
		remove_newline();

		switch(option)
		{
		case 1:
			if (racer_num < 10)
			{
				racers[racer_num] = malloc(0x100);
				printf("Name for new racer: ");
				scanf("%256s", racers[racer_num]);
				remove_newline();
				racer_num++;
			}
			else
				puts("Maximum 10 racers are allowed!");
			break;
		case 2:
			memset(winner, 0, sizeof(winner));
			for (unsigned int i=0; i<racer_num; i++)
			{
				args[i][0] = racers[i];
				args[i][1] = winner;
				pthread_create(&thread_id[i], NULL, (void*)race, &args[i]);
			}
			for (unsigned int i=0; i<racer_num; i++)
				pthread_join(thread_id[i], NULL);

			printf("Our winner: %s\n", winner);
			break;
		case 3:
			done = 1;
			break;
		default: 
			puts("Invalid choice!");
		}
	}
}

int main()
{
	init();
	run();
}