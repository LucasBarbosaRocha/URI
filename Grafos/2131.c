#include <stdio.h>
#include <stdlib.h>

void criaInicializaMatriz(int **mm, int linhas, int colunas, int inic);
void imprimeMatriz(int n, int **mm);
int DFSP(int **mm, int n, int *visited, int i);
int DFS(int **mm, int n, int *visited, int *cores, int i);

int main(void)
{
	int **mm, *visited;
	int n, m, i, v1, v2;


	while(scanf("%d %d", &n, &m) != EOF)
	{
		mm = malloc((n) * sizeof(int*));
		criaInicializaMatriz(mm, n, n, 0);
		visited = malloc((n) * sizeof(int*));
		for (i = 0; i < n; i++)
			visited[i] = -1;

		for (i = 0; i < m; i++)
		{
			scanf("%d %d", &v1, &v2);
			mm[v1-1][v2-1] = 1;
		}

		imprimeMatriz(n, mm);
		if (DFSP(mm, n, visited, 0) == 1)
			printf("sim\n");
		else
			printf("nao\n");

		free(mm);
		free(visited);

	}

	return 0;
}

void criaInicializaMatriz(int **mm, int linhas, int colunas, int inic)
{
	int i, j;
	for (i = 0; i < linhas; i++) {
		  mm[i] = malloc((colunas) * sizeof(int));
	}

	for (i = 0; i < linhas; ++i)
	{
		for (j = 0; j < colunas; ++j)
		{
			mm[i][j] = inic;
		}
	}
}

void imprimeMatriz(int n, int **mm)
{
	int i, j;

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			printf("%d ", mm[i][j]);
		}
		printf("\n");
	}
}

int DFSP(int **mm, int n, int *visited, int i)
{
	int j;
	int *cores = malloc((n) * sizeof(int));
	for (j = 0; j < n; j++)
		cores[j] = -1;

	for (j = i; j < n; j++)
	{
		if (visited[j] == -1)
		{
			if (DFS(mm, n, visited, cores, j) == 0)
				return 0;
		}
	}
	return 1;
}

int DFS(int **mm, int n, int *visited, int *cores, int i)
{
    int j, k;
    
	visited[i] = 1;
	if (cores[i] == -1)
		cores[i] = 1;
    
    for (k = 0; k < n; k++)
    	printf("%d ", cores[k]);
    printf("\n");

	printf("%d\n", cores[j]);
    for(j = 0; j < n; j++)
		//printf("%d %d \n", visited[j], visited[i]);
       if( !visited[j] && mm[i][j] == 1)
       {
       		if (cores[j] == -1)
       			cores[j] = 1 - cores[i];
       		else{
       			if (cores[j] == cores[i])
       				return 0;
       		}
            DFS(mm, n, visited, cores, j);
       }
    return 1;
}

