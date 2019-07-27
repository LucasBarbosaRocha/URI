#include <stdio.h>
#define MAX 12

int main(void)
{
	float soma, value, cont = 0;
	char op;
	int i, j, lim = MAX-1;

	scanf("%c", &op);


	soma = 0;
	for (i = 0; i < MAX; i++)
	{
		for (j = 0; j < MAX; j++)
		{
			scanf("%f", &value);
			if(j < lim){
				soma += value;
				cont++;
			}
		}
		lim--;
	}
	
	if(op == 'S')
		printf("%.1f\n", soma);
	else
		printf("%.1f\n", soma/cont);

	return 0;
}