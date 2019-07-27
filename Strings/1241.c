#include <stdio.h>
#include <string.h>

int main(void)
{
	int n, tam1, tam2, cont;
	char n1[1001], n2[1001];

	scanf("%d", &n);

	while(n-- > 0)
	{
		scanf("%s %s", n1, n2);
		tam1 = strlen(n1)-1;
		tam2 = strlen(n2)-1;

		cont = 0;
		while(tam2 >= 0 && n1[tam1] == n2[tam2])
		{
			cont++;
			tam1--;
			tam2--;
		}

		if(tam2 < 0)
			printf("encaixa\n");
		else
			printf("nao encaixa\n");

	}	

	return 0;
}
