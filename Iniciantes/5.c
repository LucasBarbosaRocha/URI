#include <stdio.h>

int main(void) {
	double a, b, media;
	scanf("%lf %lf", &a, &b);
	a = a * 3.5;
	b = b * 7.5;
	media = (a+b)/11;
	printf("MEDIA = %.5lf\n", media);
return 0;	
}