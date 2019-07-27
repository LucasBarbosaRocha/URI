#include <stdio.h>

long long int calcFat(long long int n);

int main(void) 
{
	long long int n, m, soma;

	
	while(scanf("%d %d", &n, &m) != EOF)
	{

		soma = calcFat(n) + calcFat(m);
		printf("%d\n", soma);
	}
	return 0;
}

long long int calcFat(long long int n)
{
	int i, fat = 1;

	for(i = n; i > 0; i--)
		fat = fat * i;
	return fat;
}