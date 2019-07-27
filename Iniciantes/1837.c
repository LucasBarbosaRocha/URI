n#include <stdio.h>


int main(void) {

	int dividendo, divisor, q, r;

	scanf("%d %d", &dividendo, &divisor);

	q = dividendo/divisor;
	r = dividendo%divisor;

	if (r < 0) {
		if (divisor > 0)
			q += (-1);
		if (divisor < 0)
			q -= (-1);

		r = dividendo - (divisor*q);
	}

	printf("%d %d\n", q, r);
	return 0;
}