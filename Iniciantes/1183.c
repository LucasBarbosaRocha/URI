#include <stdio.h>
#define MAX 12

int main(void)
{

	int i, iniI, j, iniJ, qtd=0;
	float m[MAX][MAX], soma;
	char op;

	scanf("%c", &op);

	for(i = 0; i < MAX; i++)
		for(j= 0; j < MAX; j++)
			scanf("%f", &m[i][j]);

	iniI = 0;
	iniJ = 1;
	for(i = iniI; i < MAX; )
	{
		for(j= iniJ; j < MAX; j++)
		{
			soma += m[i][j];
			qtd++;
		}
		i = ++iniI;
		j = ++iniJ;
	}

	if(op == 'S')
	{
		printf("%.1f\n", soma);
	}else {
		printf("%.1f\n", (soma/qtd));
	}

	return 0;
}