#include <stdio.h>
#include <iostream>

using namespace std;

int main(void)
{
	int t, n, aux, numero, media, soma, qtd, maior, maiorQtd, caso = 1;
	int p[100001];

	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d", &n);
		maior = numero = -1;
		qtd = 1;
		media = 0;
		maiorQtd = 0;
		soma = 0;
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &aux);
			p[j] = aux;
		}

		numero = p[0];
		for (int j = 1; j < n; j++)
		{
			if (numero == p[j])
			{
				qtd++;
			}else {
				//cout << p[j] << "!=" << p[j+1] << endl;
				//cout << numero << ">" << maior << ":" << qtd << " > " << maiorQtd << endl;
				if (numero > maior)
				{
					maior = numero;
					maiorQtd = qtd;						
				}
				else{
					if (numero == maior && qtd >= maiorQtd)
					{
					maior = numero;
					maiorQtd = qtd;
					}
				}
				qtd = 1;
			}
			numero = p[j];		
		}	

		//cout << numero << ">" << maior << ":" << qtd << " > " << maiorQtd << endl;
		if (numero > maior)
		{
			maior = numero;
			maiorQtd = qtd;						
		}
		else{
			if (numero == maior && qtd >= maiorQtd)
			{
			maior = numero;
			maiorQtd = qtd;
			}
		}

		printf("Caso #%d: %d\n", caso++, maiorQtd);
	}

	return 0;
}