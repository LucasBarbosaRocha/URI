#include <stdio.h>
#define MAX 51

int ordenarContar(int v[MAX], int tam);

int main(void)
{
	int v[MAX], i, j, l, n, number, resultado;

	scanf("%d", &n);

	while (n-- > 0)
	{
		scanf("%d", &l);
		for (i = 0; i < l; i++)
		{
			scanf("%d", &number);
			v[i] = number;
		}
		resultado = ordenarContar(v, l);
		printf("Optimal train swapping takes %d swaps.\n", resultado);

	}
	return 0;
}

int ordenarContar(int v[MAX], int tam)
{
	int i, j, number, trocas = 0;

	for (i = 1; i < tam; i++)
	{
		number = v[i];
		for (j = i - 1; j >= 0 && v[j] > number; j--)
		{
			v[j+1] = v[j];
			trocas++;
		}
		v[j+1] = number;
	}

	return trocas;
}
