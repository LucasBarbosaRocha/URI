#include <stdio.h>
#define MAX 10001

int conta(int vetor[MAX], int n);
void troca(int *a, int *b);

int main(void)
{
	int i, j, t, n, number, result, vetor[MAX], vetorOrdenado[MAX];

	scanf("%d", &t);

	while (t-- > 0)
	{
		scanf("%d", &n);
		for (i = 0; i < n; i++)
		{
			scanf("%d", &number);
			vetor[i] = number;
			vetorOrdenado[i] = i+1;
		}

		result = conta(vetor, n);
		printf("%d\n", result);
	}
	return 0;
}

/* Selection sort */
int conta(int vetor[MAX], int n)
{
	int i, j, min, cont = 0;

	for (i = 0; i < n; i++)
	{
		min = i;
		for (j = i + 1; j < n; j++)
		{
			if (vetor[j] < vetor[min])
				min = j;
		}

		if (vetor[i] != vetor[min])
		{
			troca(&vetor[i], &vetor[min]);
			cont++;
		}
	}
	return cont;
}

void troca(int *a, int *b)
{
	int aux;
	aux = *a;
	*a = *b;
	*b = aux;
}