/*
* Nome: Lucas Barbosa Rocha
* Esse codigo consiste em verificar se o grafo eh bipartido
* Resolução:
* Foi usado DFS para varrer o grafo e verificar se eh 
* possivel pintar o grafo com duas cores
*/

#include <iostream>
#include <stdio.h>
#include <list>
#include <stack> // pilha para usar na DFS

using namespace std;

class Grafo
{
public:
	int V; 									// número de vértices
	list<int> *adj; 						// ponteiro para um array contendo as listas de adjacências

public:
	Grafo(int V); 						  	// construtor
	void adicionarAresta(int v1, int v2); 	// adiciona uma aresta no grafo
	int obterGrauDeSaida(int v);
	void imprimirGrafo();
	bool dfs(int v);

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

int Grafo::obterGrauDeSaida(int v)
{
	return adj[v].size();
}

void Grafo::imprimirGrafo()
{
	list<int >::iterator it;
	for (int i = 0; i < this->V; i++)
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

/* Percorrer o grafo em profundidade e pintar ele com apenas duas cores
* O vertice inicial eh 1, os outros sao intercalados, sua adj. eh 0, a adj. da adj. eh 1 etc..
*/
bool Grafo::dfs(int v)
{
	stack<int> pilha;
	bool visitados[V]; 
	int cores[V];
 
	// marca todos como não visitados e com a cor -1
	for(int i = 0; i < V; i++){
		visitados[i] = false;
		cores[i] = -1;
	}
 

 	for (int j = v; j < V; j++)
 	{
 		v = j;
 		if ( visitados[v] == false)
 		{
 			cores[v] = 1;
			while(true)
			{
				if(!visitados[v])
				{
					visitados[v] = true; 			// marca como visitado
					pilha.push(v); 					// insere 'v' na pilha
				}
		 
				bool achou = false;
				list<int>::iterator it;
		 
				// busca por um vizinho não visitado
				for(it = adj[v].begin(); it != adj[v].end(); it++)
				{
					if (cores[*it] == -1) 			 // Verifica se a adj. estah sem cor
						cores[*it] = 1 - cores[v];
					else if (cores[*it] == cores[v]) // Se jah tiver cor mas for igual ao pai, deu ruim
						return false;
					if(!visitados[*it])
					{
						achou = true;
						break;
					}
				}
		 
				if(achou){
					v = *it; 						 // atualiza o "v"
				}
				else
				{
					// se todos os vizinhos estão visitados ou não existem vizinhos - remove da pilha
					pilha.pop();
					// se a pilha ficar vazia, então terminou a busca
					if(pilha.empty())
						break;
					// se chegou aqui, é porque pode pegar elemento do topo
					v = pilha.top();
				}
			}
		}
	}
	return true;
}
int main()
{
	int n, m, v1, v2, k = 1, inicial;

	//cin >> n;
	// !cin.eof()
	while(scanf("%d%d", &n, &m) != EOF)
	{
		//cin >> m;
		Grafo grafo(n+1);

		for (int i = 0; i < m; i++)
		{
			//cin >> v1;
			//cin >> v2;
			scanf("%d%d", &v1, &v2);
			grafo.adicionarAresta(v1, v2);
			grafo.adicionarAresta(v2, v1);
			if (i == 0)
				inicial = v1;
		}
		//grafo.imprimirGrafo();
		cout << "Instancia " << k++ << "\n";
		if(grafo.dfs(inicial))		
			cout << "sim\n\n";
		else
			cout << "nao\n\n";
		
		//cin >> n;
	}


	return 0;
}