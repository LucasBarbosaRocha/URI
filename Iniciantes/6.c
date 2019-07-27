#include <stdio.h>

int main(void) {
	double a, b, c, media;
	scanf("%lf %lf %lf", &a, &b, &c);
	a = a * 2;
	b = b * 3;
	c = c * 5;
	media = (a+b+c)/10;
	printf("MEDIA = %.1lf\n", media);
return 0;	
}