#include <stdio.h>
#include <math.h>

int main(void) {
	int raio;
	double volume, pi = 3.14159;

	scanf("%d", &raio);

	volume = (4.0/3) * pi * pow(raio, 3); 

	printf("VOLUME = %.3lf\n", volume);


	return 0;
}