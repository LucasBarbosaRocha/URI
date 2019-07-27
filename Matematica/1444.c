#include <stdio.h>

int main(void)
{
	int n, resto, quociente, quocienteAux, aux, result;

	scanf("%d", &n);

	while (n != 0)
	{
		quociente = n / 3;
		while (n > 1)
		{
			if (n - (quociente * 3) > 2) /* Tem mais valor em n para o 2 */
			{
				quocienteAux = n - (quociente * 3);
				quocienteAux = quocienteAux / 2;
				n = quociente + quocienteAux;
				result = result + n;
				quociente = n / 3;
			} else {
				quociente = quociente - 1;
			}
		}
		printf("%d\n", result);
		result = 0;
		scanf("%d", &n);
	}

	return 0;
}