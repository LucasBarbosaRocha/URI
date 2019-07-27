/*Bhaskara*/
#include <stdio.h>
#include <math.h>

int main(void) {
	double a, b, c, delta = 0, R1, R2;

	scanf("%lf %lf %lf", &a, &b, &c);

	if ((2*a) != 0) { /* Divisão por zero não pode*/

		delta = (b*b) - (4*a*c);

		if(delta >= 0) { /* Delta menor que 0 sem raizes reais*/

			R1 = ((b*(-1)) + sqrt(delta)) / (2*a);
			R2 = ((b*(-1)) - sqrt(delta)) / (2*a);

			printf("R1 = %.5lf\n", R1);
			printf("R2 = %.5lf\n", R2);

		} else {
			printf("Impossivel calcular\n");
		}

	} else {
			printf("Impossivel calcular\n");	
	}

	return 0;
}