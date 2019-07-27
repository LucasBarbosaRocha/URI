#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int subSequencia(char *u, char *v, int tamU, int tamV);

int main(void)
{
	char *u, *v, a;
	int tamU, tamV, resposta;



		u = (char *)(malloc ((101) * sizeof(char)));
		v = (char *)(malloc ((101) * sizeof(char)));
	
	while(fgets(u, 100, stdin) && fgets(v, 100, stdin))
	{
		tamU = strlen(u);
		tamV = strlen(v);

		if (u[tamU  - 1] == '\n')
			u[tamU--] = 0;
		if (v[tamV  - 1] == '\n')
			v[tamV--] = 0;

		resposta = subSequencia(u, v, tamU, tamV);
		printf("%d\n", resposta);


	}
	
	return 0;
}

int subSequencia(char *u, char *v, int tamU, int tamV)
{
	int resposta, i, j, r, h;
	
	resposta = 0;
	for (i = 0; i < tamU; i++) 
	{
		for (j = 0; j < tamV; j++) 
		{
			if (u[i] == v[j]) 
			{
				r = 0;
				for (h = 0; h+i<tamU, h+j<tamV; h++) 
				{
					if (u[h+i] != v[h+j])
						break;
					r++;
				}
				if (r > resposta)
				resposta = r;
			}
		}
	}
	return resposta;
}