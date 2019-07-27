#include <stdio.h>

int tamanho(char *c);
int verificaLetra(char c);
void inverte(char *c);
void trunca(char *c);
int main(void)
{
	char m[1000];
	int i, j, n;

	scanf("%d ", &n);


	for (i = 0; i < n; i++)
	{
		j = 0;
		do{
			scanf("%c", &m[j]);
			j++;
		}while(m[j-1] != '\n');

		/* Primeira verificacao */
		j = 0;
		do{
			if(verificaLetra(m[j]))
				m[j] = m[j]+3;
			j++;
		}while(m[j-1] != '\n');		

		/* Segunda Verificacao */
		inverte(m);

		/* Terceira Verificacao */
		trunca(m);
		j = 0;
		do{
			printf("%c", m[j]);
			j++;
		}while(m[j] != '\n');
		printf("\n");
	}



	return 0;
}

int tamanho(char *c)
{
	int j = 0;
	do{
		j++;
	}while(c[j]!= '\n');
	return j;
}

int verificaLetra(char c)
{
	int i;
	char *d;
	d = "abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXWYZ";
	for(i = 0; i < 52; i++)
	{
		if(c == d[i])
			return 1;
	}
	return 0;

}

void inverte(char *c)
{
	int i = 0, tam = tamanho(c)-1;
	char bkp;
	
	do{
		bkp = c[i];
		c[i] = c[tam];
		c[tam] = bkp;
		i++; tam--;
	}while(i < tam);
}

void trunca(char *c)
{
	int tam = tamanho(c), i = tam/2;
	for(; i < tam; i++)
		c[i] = c[i] - 1;
}