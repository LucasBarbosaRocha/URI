#include <stdio.h>

int main(void)
{
	int n, cont = 1, i, r, razao;

	scanf("%d", &n);

	while (n != 0)
	{
		printf("Teste %d\n", cont++);
		r = 1;
		razao = 2;
		for (i = 1; i < n; i++)
		{
			r += razao;
			razao = razao*2;
		}
		printf("%d\n\n", r);
		scanf("%d", &n);
	}


	return 0;
}