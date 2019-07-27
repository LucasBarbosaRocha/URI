#include <stdio.h>

int main(void)
{
	int n, dias;
	float valor, aux;

	scanf("%d", &n);
	while (n-- > 0)
	{
		dias = 0;
		scanf("%f", &valor);

		while (valor > 1)
		{
			dias++;
			valor *= 0.5;
		}
		printf("%d dias\n", dias);

	}

	return 0;
}