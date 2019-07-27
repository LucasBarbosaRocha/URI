#include <stdio.h>
#include <math.h>

int main(void) {
	float x1, x2, y1, y2, distanciaEntrePontos;
	float tmp, tmp2, aux;
	scanf("%f %f", &x1, &y1);
	scanf("%f %f", &x2, &y2);
	tmp = x2 - x1;
	tmp2 = y2 - y1;
	tmp = tmp * tmp;
	tmp2 = tmp2 * tmp2;
	aux = tmp + tmp2;
	distanciaEntrePontos = sqrt(aux);

	printf("%.4f\n", distanciaEntrePontos);

	return 0;
}