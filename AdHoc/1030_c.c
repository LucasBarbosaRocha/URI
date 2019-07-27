#include <stdio.h>

int josefus(int n, int k);
int main(void)
{
	int cn, n, k, i;
	scanf("%d", &cn);
	for(i = 0; i < cn; i++)
	{
		scanf("%d%d", &n, &k);
		printf("Case %d: %d\n", (i+1), josefus(n, k));
	}
	return 0;
}

int josefus(int n, int k)
{
	if (n == 1)
		return 1;
	else
		return ((josefus(n-1, k) + k-1) %n) + 1;
}