#include <stdio.h>


int main(void) {
	int num, vector[10], i = 1;

	scanf("%d",&num);
	vector[0] = num;
	printf("N[%d] = %d\n", i-1, num);
	for (; i < 10; i++){
		num *= 2;
		vector[i] = num;
		printf("N[%d] = %d\n", i, num);
	}
	return 0;
}