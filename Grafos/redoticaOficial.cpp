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




int main()
{
	int n, m, u, v, v1, v2, peso, custoMinimo = 24;
	int grafoBKP[tam][tam];

	scanf("%d%d", &n, &m);
	while (n != 0 && m != 0)
	{
		Grafo grafo(n+1);


		for (int i = 0; i < m; i++)
		{
			scanf("%d%d%d", &v1, &v2, &peso);
			grafo.adicionarAresta(v1, v2, peso);
			grafo.adicionarAresta(v2, v1, peso);

		}

		grafo.imprimirGrafo();
		
		scanf("%d%d", &n, &m);
	}

	return 0;
}