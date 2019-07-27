#include <stdio.h>
#include <stdlib.h>

void randomVetor(int *array, int S, int N)
{
	int i;
	array[0] = S;
	for (i = 1; i < N; ++i)
    	array[i] = (1LL*array[i-1]*1103515245 + 12345) % (2147483648LL);
}

void imprime(int *array, int N)
{
	int i;
	for (i = 0; i < N; i++)
		printf("%d ", array[i]);
	printf("\n");
}

int main(void)
{
	int T, N, K, S, *array, i;


	scanf("%d", &T);
	while (T-- > 0)
	{
		scanf("%d%d%d", &N, &K, &S);
		array = malloc(N * sizeof(int));
		randomVetor(array, S, N);
		//imprime(array, N);



	}


	return 0;
}