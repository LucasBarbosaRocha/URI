#include <stdio.h>

int main(void)
{
	int n, i;
	char frase[101], time1[101], time2[101];

	scanf("%d ", &n);

	for (i = 0; i < n; i++)
	{
		scanf("%[^\n] %[^\n] %[^\n]", frase, time1, time2);
		printf("%s\n%s\n%s", frase, time1, time2);


		
		
	}


	return 0;
}