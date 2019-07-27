/*
* PEDAFIO
* Nome: Lucas Barbosa Rocha
* Esse codigo consiste em verificar se o grafo eh bipartido
* Resolução:
* Foi usado BFS para varrer o grafo e distribuir as distancias 
* no final varremos o vetor respostas pegando todas adjacencias
* menores que o custo total
*/



#include <iostream>
#include <stdio.h>
#include <list>
#include <stack> // pilha para usar na DF

using namespace std;

class Grafo
{
public:
	int V; 									// número de vértices
	list<int> *adj; 						// ponteiro para um array contendo as listas de adjacências

public:
	Grafo(int V); 						  	// construtor
	void adicionarAresta(int v1, int v2); 	// adiciona uma aresta no grafo
	list<int> bfs(int v, int custo);

};

Grafo::Grafo(int V)
{
	this->V = V; 							// atribui o número de vértices
	adj = new list<int>[V]; 				// cria as listas
}

void Grafo::adicionarAresta(int v1, int v2)
{
	adj[v1].push_back(v2);
}

list<int> Grafo::bfs(int v, int custo)
{
	list<int> lista;
	list<int> resposta;
	list<int>::iterator it;
	bool visitados[V];
	int resultados[V];
 
	// marca todos como não visitados
	for(int i = 0; i < V; i++){
		visitados[i] = false;
		resultados[i] = 0;
	}

	visitados[v] = true;
	lista.push_back(v);
	while (!lista.empty())
	{
		v = lista.front();
		lista.pop_front();
		for(it = adj[v].begin(); it != adj[v].end(); it++)
		{
			if (visitados[*it] == false)
			{
				visitados[*it] = true;
				resultados[*it] = resultados[v] + 1;
				lista.push_back(*it);
			}
		}
	}

	for (int i = 0; i < V; i++)
	{
		if (resultados[i] != 0 && resultados[i] <= custo){
			resposta.push_back(i);
		}
	}

	resposta.sort();
 return resposta;
}


int main()
{
	int C, E, L, P, v1, v2, kk = 1;


	scanf("%d%d%d%d", &C, &E, &L, &P);
	
	while(C != 0 && E != 0 && L != 0 && P != 0)
	{

		Grafo grafo(C+1);

		for (int i = 0; i < E; i++)
		{
			scanf("%d%d", &v1, &v2);
			grafo.adicionarAresta(v1, v2);
			grafo.adicionarAresta(v2, v1);

		}


		printf("Teste %d\n", kk++);
		list<int> l = grafo.bfs(L, P);

		list<int>::iterator it;
		for(it = l.begin(); it != l.end(); it++)
			printf("%d ", *it);

		printf("\n\n");
		scanf("%d%d%d%d", &C, &E, &L, &P);
	}
	return 0;
}