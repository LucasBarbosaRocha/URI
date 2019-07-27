#include <stdio.h>

int main(void) {
	float salario, reaj;
	int perc;
	scanf("%f", &salario);

	if (salario <= 400){
		reaj = salario * 0.15;
		perc = 15;
	}else {
		if (salario > 400 && salario <= 800) {
			reaj = salario * 0.12;
			perc = 12;
			} else {
				if (salario > 800 && salario <= 1200){
					reaj = salario * 0.10;
					perc = 10;
					} else {
						if (salario > 1200 && salario <= 2000) {
							reaj = salario * 0.07;
							perc = 7;
						} else {
							if (salario > 2000){
								reaj = salario * 0.04;
								perc = 4;
								}
							}
						}
					}
		}	

	printf("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %%\n", (salario+reaj), reaj, perc);

	return 0;
}