#include <stdio.h>
#include <stdlib.h>
#define PI 3.14159

double calculaArea(int tipo, double ladoA, double ladoB, double altura) {

	switch(tipo) {
		/* Tipo 0  Base*Altura / 2*/
		case 0: /* Area do Triangulo base ladoA*/
		return (ladoA*altura)/2;
		/* Tipo 1 PI * raio² */
		case 1: /* Area do circulo, o raio é a variavel altura*/
		return PI*(altura*altura);
		/* Tipo 2 ((base1 + base2) * altura) / 2 */
		case 2: /* Area do Trapezio*/
		return ((ladoA+ladoB)*altura)/2;
		/* Tipo 3 LadoA * ladoB */
		case 3: /* Area do Quadrado exemplo ladoB*/
		return ladoB*ladoB;
		/* Tipo 4 base*Altura */
		case 4: /* Area do Retangulo*/
		return ladoA*ladoB;
		default:
		return 0;
	}
}
int main(void) {

	double a, b, c;
	scanf("%lf %lf %lf", &a, &b, &c);

	printf("TRIANGULO: %.3lf\nCIRCULO: %.3lf\nTRAPEZIO: %.3lf\nQUADRADO: %.3lf\nRETANGULO: %.3lf\n", calculaArea(0,a,b,c), calculaArea(1,a,b,c), calculaArea(2,a,b,c), calculaArea(3,a,b,c), calculaArea(4,a,b,c));
	return 0;
}