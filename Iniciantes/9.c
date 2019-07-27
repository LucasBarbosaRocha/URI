#include <stdio.h>
#include <string.h>

int main(void) {	
	char nome[20];
	double salario, totalVendas;

	scanf("%s %lf %lf", &nome, &salario, &totalVendas);
	printf("TOTAL = R$ %.2lf\n", salario + (totalVendas * 0.15));

	return 0;
}