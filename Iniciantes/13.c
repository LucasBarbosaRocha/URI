#include <stdio.h>

int maior(int a, int b) {
	int	c = a - b;
	if (c < 0)
		c = c * (-1);
	return (a+b+c)/2;
}

int main(void) {

	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	printf("%d eh o maior\n", maior(maior(a,b),c));
return 0;
}