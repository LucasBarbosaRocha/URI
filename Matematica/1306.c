#include <stdio.h>
#include <math.h>

int main(void)
{
	int r, n, aux, cont = 1;
	double valor;

	scanf("%d%d", &r, &n);

	while (r != 0 && n != 0)
	{
		if (r >= n)
			aux = r - n;
		else
			aux = r;	
		valor = ceil((double)aux / n);
		if (r < n || (r < n && n <= 26))
			printf("Case %d: 0\n", cont++);
		else if (valor <= 26)
			printf("Case %d: %d\n", cont++, (int) valor);
		else
			printf("Case %d: impossible\n", cont++);



		scanf("%d%d", &r, &n);		
	}


	return 0;
}