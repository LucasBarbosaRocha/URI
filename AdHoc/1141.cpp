#include <stdio.h>

using namespace std;

int main(void)
{
	int h, d, maior;

	while(1)
	{
		scanf("%d", &h);
		if (h == 0)
			break;

		maior = h;

		while(h > 1)
		{
			if (h % 2 == 0)
				d = h * 0.5;
			else
				d = (h * 3) + 1;

			if (d > maior)
				maior = d;

			h = d;
		}

		printf("%d\n", maior);
	}



	return 0;
}