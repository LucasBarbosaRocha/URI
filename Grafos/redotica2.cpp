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
	int u;
	int v;
	int pes;
public:
   Node(int _v, int _pes)
   {
		v = _v;
		pes = _pes;
   }
   Node(int _u, int _v, int _pes)
   {
		u = _u;
		v = _v;
		pes = _pes;
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
	int *pai;
public:
	// Construtor 
	Grafo(int V); 				
	// adiciona uma aresta no grafo		  	
	void adicionarAresta(int v1, int v2, int peso);
	// Funcao calcula o caminho minimo para um v fonte 	
	void prim(int fonte);
	// Funcao que imprime o grafo
	void imprimirGrafo();
	void imprimirDistancia();
	void imprimirFinal();
	void imprimirSolucao();
};

Grafo::Grafo(int V)
{
	this->V = V; 							// atribui o número de vértices
	adj = new list<Node>[V]; 				// cria as listas
	dist = new int[V];
	pai = new int[V];
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
			cout << (*it).v << " ";
		}
		cout <<"\n";
	}
	cout << "\n";
}

void Grafo::imprimirDistancia()
{
	list<int >::iterator it;

	for (int i = 0; i < this->V; i++)
	{
		//cout << this->dist[i] << " ";
		printf("(%d,%d) = %d\n", i, this->pai[i], this->dist[i]);
	}
	cout <<"\n";
}

void Grafo::imprimirSolucao()
{
	std::list<Node> final;
	int val[this->V][this->V];

	for (int i = 0; i < this->V; i++)
		for (int j = 0; j < this->V; j++)
			val[i][j] = 0;

	for (int i = 0; i < this->V; i++)
	{
		if (this->dist[i] > 0 && this->dist[i] < 100000)
		{
			//printf("(%d,%d) = %d\n", min(i, this->pai[i]), max(i, this->pai[i]), this->dist[i]);
			//printf("%d %d\n", min(i, this->pai[i]), max(i, this->pai[i]));
			if (val[this->pai[i]][i] == 0 || val[i][this->pai[i]] == 0)
			{
				Node node(min(i, this->pai[i]), max(i, this->pai[i]),dist[i]);
				final.push_back(node);
				val[this->pai[i]][i] = 1;
				val[i][this->pai[i]] = 1;
			}
		}
	}


	list<Node >::iterator it;
	final.sort([](const Node &f, const Node &s) { return f.pes < s.pes; });

	for (it = final.begin(); it != final.end(); it++)
	{
		printf("%d %d\n", (*it).u, (*it).v);
	}
	cout <<"\n";

}

void Grafo::prim(int fonte)
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
        // has to be done this way to keep the vs
        // sorted distance (distance must be first item
        // in pair)
        int u = pq.top().v;
        pq.pop();
        menores.push_back(u);
 
        // Verificando as adjacencias
        list<Node>::iterator i;
        for (i = adj[u].begin(); i != adj[u].end(); ++i)
        {
            int v = (*i).v;
            int weight = (*i).pes; // w(uv)
 
            if (weight < dist[v])
            {
                dist[v] = weight;
                pai[v] = u;
                pq.push(Node(v, dist[v]));
                //final.push_back(Node(u,v,dist[v]));
            }
        }
    }
}



int main(void)
{
	int n, m, x, v, p, c = 1;

	scanf("%d%d", &n, &m);
	while(n != 0 && m != 0)
	{
		Grafo grafo(n+1);

		for (int i = 0; i < m; i++)
		{
			scanf("%d%d%d", &x, &v, &p);
			//grafo[x-1][v-1] = p;
			grafo.adicionarAresta(x, v, p);
			grafo.adicionarAresta(v, x, p);
		}

		grafo.imprimirGrafo();

		grafo.prim(1);
		printf("Teste %d\n", c++);
		grafo.imprimirDistancia();
		grafo.imprimirSolucao();

		scanf("%d%d", &n, &m);


	}


	return 0;
}


