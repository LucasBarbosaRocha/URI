#include <stdio.h>

int main(void)
{
	int entrada, n, i;
	scanf("%d", &n);

	for(i = 0; i < n; i++)
	{
		scanf("%d", &entrada);

		if (entrada % 4 == 0)
			printf("1\n");
		else if (entrada % 4 == 1)
			printf("7\n");
		else if (entrada % 4 == 2)
			printf("9\n");
		else if (entrada % 4 == 3)
			printf("3\n");
	}

}