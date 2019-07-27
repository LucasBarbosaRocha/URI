#include <stdio.h>

#define MAX 1000000

void troca(int *a, int *b){
    int aux;
    aux = *a;
    *a = *b;
    *b = aux;
}
int separa(int p, int r, int v[MAX]){
    int x, i, j;
    x=v[p];
    i = p - 1;
    j = r + 1;
    while(1){
        do{
            j--;
        }while(v[j]>x);
        do{
            i++;
        }while(v[i]<x);
        if(i<j)
            troca(&v[i], &v[j]);
        else
            return j;
    }
}
void quicksort(int p, int r, int v[MAX]){
    int q;
    if (p < r){
        q = separa(p, r, v);
        quicksort(p, q, v);
        quicksort(q+1, r, v);
    }
}

int main(void)
{
	int vetor[MAX], i, j, n, tam, ini, fim, p;

	while (scanf("%d", &n) != EOF)
	{
		tam = 0;
		for (i = 0; i < n; i++)
		{
			scanf("%d %d", &ini, &fim);
			for (j = ini; j <= fim; j++)
			{
				vetor[tam] = j;
				tam++;
			}
		}

		quicksort(0, tam - 1, vetor);
		scanf("%d", &p);
		i = 0;
		while (i < tam && vetor[i] != p)
			i++;
		ini = i;
		while (i < tam && vetor[i] == p)
			i++;
		fim = i;
		if (ini < fim)
			printf("%d found from %ld to %ld\n", p, ini, fim - 1);
		else
			printf("%d not found\n", p);
	}


}