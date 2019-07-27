#include <stdio.h>

int main(void)
{
	double l;
	double i, aux, x;

	scanf("%lf", &l);
	while(l != 0)
	{
		aux =  l-3;
		i = l+aux;
		x = (i-l)/l;

		printf("%.6lf\n", x);

		scanf("%lf", &l);
	}



	return 0;
}