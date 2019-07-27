#include <stdio.h>

int main(void) {
	int a, n, soma = 0, i = 0;

	scanf("%d %d", &a, &n);

	if(n <= 0)
		while(n <= 0)
			scanf("%d", &n);

	while(n-- > 0) {
		soma = soma + (a+i);
		i++;
	}
	printf("%d\n",soma);
return 0;
}