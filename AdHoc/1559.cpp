#include <iostream>
#include <stdio.h>

using namespace std;

int main(void)
{
	int n, num, matriz[4][4], vetor[4];

	scanf("%d", &n);

	while (n-- > 0)
	{

		for (int i = 0; i < 4; i++)
			vetor[i] = 0;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				matriz[i][j] = 0;
			}
		}

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%d", &num);
				matriz[i][j] = num;
			}
		}


		int aux = 0;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (matriz[i][j] != 0)
				{

					if (matriz[i][j] == 2048)
					{
						aux = 1;
					}

					if (j < 3)
					{
						if(matriz[i][j] == matriz[i][j+1] || matriz[i][j+1] == 0)
						{
							vetor[2] = 1;
						}
					}

					if (j > 0)
					{
						if(matriz[i][j-1] == matriz[i][j] || matriz[i][j-1] == 0)
						{
							vetor[1] = 1;
						}						
					}

					if(i < 3)
					{
						if(matriz[i][j] == matriz[i+1][j] || matriz[i+1][j] == 0)
						{
							vetor[0] = 1;
						}						
					}

					if(i > 0)
					{
						if(matriz[i-1][j] == matriz[i][j] || matriz[i-1][j] == 0)
						{
							vetor[3] = 1;
						}						
					}
				}
			}
		}		

		string resp = "";
		if (vetor[0] != 0)
		{
			resp = resp + "DOWN ";
		}
		if (vetor[1] != 0)
		{
			resp = resp + "LEFT ";
		}	
		if (vetor[2] != 0)
		{
			resp = resp + "RIGHT ";
		}
		if (vetor[3] != 0)
		{
			resp = resp + "UP ";
		}


		resp[resp.size()] = '\0';

		if (aux != 1 && resp != "")
			cout << resp << "\n";
		else
			printf("NONE\n");

	}
	return 0;
}