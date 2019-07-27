#include <stdio.h>
int main(void) {
	double pi = 3.14159, raio = 0, area;
	scanf("%lf", &raio);
	area = pi * (raio*raio);

	printf("A=%.4lf\n", area);

	return 0;
}