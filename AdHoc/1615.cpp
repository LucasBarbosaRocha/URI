#include <stdio.h>

using namespace std;

int main(void)
{
	int t, i, n, m, aux, ganhador, candidatos[11] = {0,0,0,0,0,0,0,0,0,0,0};
	float votos;

	scanf("%d", &t);

	i = 0;
	while (i++ < t)
	{
		scanf("%d%d", &n, &m);

		for (int j = 0; j < 11; j++)
			candidatos[j] = 0;

		for (int j = 0; j < m; j++)
		{
			scanf("%d", &aux);
			candidatos[aux] = candidatos[aux] + 1;
		}

		votos = m * 0.5;

		ganhador = -1;
		for (int j = 1; j <= n; j++)
		{
			if (candidatos[j] > votos)
				ganhador = j;
		}	

		printf("%d\n",ganhador);	
	}


	return 0;
}