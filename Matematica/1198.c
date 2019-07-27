#include <stdio.h>
#include <math.h>

int main(void)
{
	long int a, b;

	while(scanf("%d%d", &a, &b) != EOF)
	{
		printf("%d %d\n", a, b);
		printf("%d \n", abs(a-b));
	}


	return 0;
}