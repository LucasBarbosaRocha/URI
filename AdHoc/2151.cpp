#include <stdio.h>
#include <iostream>

using namespace std;

int main(void)
{
	int c, m, n, x, y;

	scanf("%d", &c);
	for (int i = 0; i < c; i++)
	{
		scanf("%d", &m);
		scanf("%d", &n);
		scanf("%d", &x);
		scanf("%d", &y);

		int matriz[m][n];

		for (int j = 0; j < m; j++)
		{
			for (int k = 0; k < n; k++)
			{
				int aux;
				scanf("%d", &aux);
				matriz[j][k] = aux;
			}
		}

		matriz[x][y] = matriz[x][y] + 10

		// m - linha n - coluna


	}
	return 0;
}