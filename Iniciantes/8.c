#include <stdio.h>

int main(void) {	
int number, horas;
	double valor;

	scanf("%d %d %lf", &number, &horas, &valor);
	printf("NUMBER = %d\n", number);
	printf("SALARY = U$ %.2lf\n", horas*valor);
	return 0;
}