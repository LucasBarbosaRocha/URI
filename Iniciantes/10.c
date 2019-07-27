#include <stdio.h>

int main(void) {
	int number1, number2, cod1, cod2;
	double val1, val2;

	scanf("%d %d %lf", &cod1, &number1, &val1);
	scanf("%d %d %lf", &cod2, &number2, &val2);

	printf("VALOR A PAGAR: R$ %.2lf\n", ((number1*val1)+(number2*val2)) );

	return 0;
}