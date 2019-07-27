/*
* REDOTICA
* Nome: Lucas Barbosa Rocha
* Solução: Rodar o PRIM para encontrar a arvore geradora minima
* Depois acrescentar todas as arestas da arvore em uma lista com tres parametros:
* (u, v, pes), e entao ordenar a lista pelo campo pes (peso)
*/
#include <iostream>
#include <stdio.h>
#include <list>
#include <values.h>
#include <stdio.h>

using namespace std;

const int INF = MAXINT/2;
#define V 102

int fixo[V];
int custo[V];
int resp[V];
int visitados[V];
list<int> *adj;

class Node
{
public:
	int u;
	int v;
	int pes;
public:
   Node(int _u, int _v, int _pes)
   {
      u = _u;
      v = _v;
      pes = _pes;
   }
};

void imprimirGrafo(list<int> *adj)
{
	list<int >::iterator it;
	for (int i = 0; i < V; i++)
	{
		cout << i << " ";
		for (it = adj[i].begin(); it != adj[i].end(); it++)
		{
			cout << (*it) << " ";
		}
		cout <<"\n";
	}
	cout << "\n";
}

/* Função PRIM encontra a arvore geradora minima */
void PRIM(int G[V][V], int inicial, int n)
{
	int total = 0;
	adj = new list<int>[n+1]; 

	for(int i = 0; i < n; i++) {
		fixo[i] = 0;
		custo[i] = INF;
		resp[i] = -1;
	}

	custo[inicial] = 0;

	for(int faltam = n; faltam>0; faltam--) 
	{
		int no = -1;
		for(int i = 0; i < n; i++){
			if(!fixo[i] && (no==-1 || custo[i] < custo[no]))
				no = i;
		}
		fixo[no] = 1;
		visitados[no] = 1;

		if(custo[no] == INF) {
			total = INF;
			break;
		}
		total += custo[no];
		for(int i = 0; i < n; i++)
		{
			if (G[no][i] != 0)
			{

				if(custo[i] > G[no][i]){
					custo[i] = G[no][i];
					resp[i+1] = no+1;
				}
			
			}
		}
	}
		
	
}

int main(void)
{
	int n, m, x, v, p, c = 1;
	int grafo[V][V];
	int val[V][V];

	scanf("%d%d", &n, &m);
	while(n != 0 && m != 0)
	{

		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				grafo[i][j] = 0;
				val[i][j] = 0;
				visitados[j] = 0;
			}
		}

		for (int i = 0; i < m; i++)
		{
			scanf("%d%d%d", &x, &v, &p);

			grafo[x-1][v-1] = p;
			grafo[v-1][x-1] = p;
		}

		printf("Teste %d\n", c++);
		for (int j = 1; j < n; j++)
		{
			if (visitados[j] == 0)
			{
				PRIM(grafo, j, n);

				std::list<Node> final;

				for (int i = 1;i <= n; i++)
				{
					if (resp[i] != -1)
					{
						Node node(min(resp[i], i),max(resp[i], i),custo[i-1]);
						final.push_back(node);	
						val[resp[i]][i] = 1;
						val[i][resp[i]] = 1;
					}
				}

				list<Node >::iterator it;

				for (it = final.begin(); it != final.end(); it++)
				{
					if ( (*it).u != (*it).v && (*it).u != 0 && (*it).v != 0)
						printf("%d %d\n", min((*it).u, (*it).v), max((*it).u, (*it).v));
				}	
			}
		}
		printf("\n");
		scanf("%d%d", &n, &m);
	}

	return 0;
}


