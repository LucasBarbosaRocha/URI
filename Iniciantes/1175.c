#include <stdio.h>
#include <stdlib.h>
#define max 20

void troca(int *a, int *b) {
	int c;
	c = *a;
	*a = *b;
	*b = c;
}

int main(void) {

	int i = 0, v[max];
	for (; i < max; i++)
		scanf("%d", &v[i]);

	for(i = 0; i < (max/2); i++){
		troca(&v[i], &v[max-i-1]);
	}

	for(i = 0; i < max; i++)
		printf("N[%d] = %d\n", i, v[i]);

	return 0;
}