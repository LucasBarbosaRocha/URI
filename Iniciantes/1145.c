#include <stdio.h>

int main(void) {
	int x, y, i = 1, cont = 0;

	scanf("%d %d", &x, &y);

	while (i <= y) {
		printf("%d", i);
		cont++;
		if (cont == x) {
			printf("\n");
			cont = 0;
		} else
			printf(" ");
		i++;
	}
return 0;
}