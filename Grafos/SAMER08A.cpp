/*
* SAMER08A
* Nome: Lucas Barbosa Rocha
* Esse codigo consiste em verificar se o grafo eh bipartido
* Resolução: Usar o Dijkstra para encontrar o custo do caminho minimo
* 1 - Usar o Dijkstra para encontrar o novo caminho minimo do grafo
* 2 - Usar o Dijkstra para encontrar o novo caminho minimo do grafo Reverso
* 3 - Agora percorra o grafo original verificando o custo de chegar da origem 
* para cada i, e soma com o custo para chegar do destino ate esse mesmo i
* se der igual o custo minimo, nao add. essa aresta, caso contrario coloque ela
* 4 - Usar o Dijkstra para encontrar o novo caminho minimo no novo grafo
*/
#include <iostream>
#include <stdio.h>
#include <list>
#include <stack> // pilha para usar na DF
#include <bits/stdc++.h>
#include <values.h>


using namespace std;
#define tam 1000
const int INF = MAXINT/2;

class Node
{
public:
	int vertice;
	int pes;
	int zoado;
public:
   Node(int _vertice, int _pes)
   {
      vertice = _vertice;
      pes = _pes;
      zoado = 0;
   }
};

class myComparator
{
public:
    int operator() (Node n1, Node n2)
    {
        return n1.pes > n2.pes;
    }
};

class Grafo
{
public:
	int V; 									// número de vértices
	list<Node> *adj; 						// ponteiro para um array contendo as listas de adjacências
	int *dist;
public:
	// Construtor 
	Grafo(int V); 				
	// adiciona uma aresta no grafo		  	
	void adicionarAresta(int v1, int v2, int peso);
	// Funcao calcula o caminho minimo para um vertice fonte 	
	void dijkstra(int fonte, int destino);
	// Funcao que imprime o grafo
	void imprimirGrafo();
	// Funcao constroi um grafo sem o(s) caminho(s) minimo(s)
	Grafo constroiGrafoSemCaminhoMinimo(int grafoBKP[tam][tam], Grafo R, int destino);
};

Grafo::Grafo(int V)
{
	this->V = V; 							// atribui o número de vértices
	adj = new list<Node>[V]; 				// cria as listas
	dist = new int[V];
}

void Grafo::adicionarAresta(int v1, int v2, int peso)
{
	Node node(v2, peso);
	adj[v1].push_back(node);
}

void Grafo::imprimirGrafo()
{
	list<Node >::iterator it;
	for (int i = 0; i < this->V; i++)
	{
		cout << i << " ";
		for (it = adj[i].begin(); it != adj[i].end(); it++)
		{
			cout << (*it).vertice << " ";
		}
		cout <<"\n";
	}
	cout << "\n";
}

Grafo Grafo::constroiGrafoSemCaminhoMinimo(int grafoBKP[tam][tam], Grafo grafoR, int destino)
{
	list<Node >::iterator it;
	Grafo grafoF(this->V);
	for (int i = 0; i < this->V; i++)
	{
		for (it = this->adj[i].begin(); it != this->adj[i].end(); it++)
		{
	        /* Note que essa diferenca verifica se existe um caminho que 
	        ao combinar metade do caminho com a distancia do original
	        com a do Reverso der o peso minimo nao deve inserir ele no grafo
	        */
			if (this->dist[i] + grafoBKP[i][(*it).vertice] + grafoR.dist[(*it).vertice] != this->dist[destino])
			{
				grafoF.adicionarAresta(i, (*it).vertice, (*it).pes);
			}
		}
	}
	return grafoF;
}

void Grafo::dijkstra(int fonte, int destino)
{
    // Heap de prioridades
    priority_queue< Node, vector <Node> , myComparator > pq;
 
    // Vetor dist com distancias infinitas
    //int dist[V];
    list<int> menores;

    for (int j = 0; j < V; j++)
    {
    	dist[j] = 100000;
    }
 
    // node inicial com distancia 0 na heap

    pq.push(Node(fonte, 0));
    dist[fonte] = 0;
 
    /* Rodar enquanto a lista de prioridades nao fica vazia */
    while (!pq.empty())
    {
        // The first vertex in pair is the minimum distance
        // vertex, extract it from priority queue.
        // vertex label is stored in second of pair (it
        // has to be done this way to keep the vertices
        // sorted distance (distance must be first item
        // in pair)
        int u = pq.top().vertice;
        pq.pop();
        menores.push_back(u);
 
        // Verificando as adjacencias
        list<Node>::iterator i;
        for (i = adj[u].begin(); i != adj[u].end(); ++i)
        {
            int v = (*i).vertice;
            int weight = (*i).pes;
 
            if (dist[v] > dist[u] + weight)
            {
                dist[v] = dist[u] + weight;
                pq.push(Node(v, dist[v]));
            }
        }
    }
}

int main()
{
	int n, m, u, v, v1, v2, peso, custoMinimo = 24;
	int grafoBKP[tam][tam];

	scanf("%d%d", &n, &m);
	while (n != 0 && m != 0)
	{
		scanf("%d%d", &u, &v);
		Grafo grafo(n+1);
		Grafo grafoR(n+1);
		Grafo grafoF(n+1);

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				grafoBKP[i][j] = INF;

		for (int i = 0; i < m; i++)
		{
			scanf("%d%d%d", &v1, &v2, &peso);
			grafoBKP[v1][v2] = peso;
			grafo.adicionarAresta(v1, v2, peso);
			grafoR.adicionarAresta(v2, v1, peso);
		}
		grafo.dijkstra(u, v); 
		grafoR.dijkstra(v, u);  
		grafoF = grafo.constroiGrafoSemCaminhoMinimo(grafoBKP,grafoR, v);
		grafoF.dijkstra(u, v);

		if (grafoF.dist[v] > 10000)
			printf("-1\n");
		else
			printf("%d\n", grafoF.dist[v]);
		scanf("%d%d", &n, &m);
	}

	return 0;
}