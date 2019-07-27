/*
* WORDS1 - Play on Words
* Nome: Lucas Barbosa Rocha
* Esse codigo consiste em verificar se o grafo permite uma trilha aberta euleriana
* Resolução:
* Trilhas eulerianas, se o grafo for desconexo não tem trilha
* verificar os pesos e garantir que só os extremos fiquem com grau irregular
*/
 
#include <iostream>
#include <stdio.h>
#include <list>
#include <queue>
#include <string.h>
#include <vector>
#include <map>

 
using namespace std;
 
// variáveis usadas -------------
int g[27][27];
bool found[26];
//-------------------------------
 
class Grafo
{
public:
    int V;                                // número de vértices
    list<int> *adj;                       // ponteiro para um array contendo as listas de adjacências
 
public:
    Grafo(int V);                           // construtor
    void adicionarAresta(int v1, int v2);   // adiciona uma aresta no grafo
    list<int> bfs(int v, int custo);
    int devolveIndice(char letra);
    void imprimirGrafo();
    void achaCaminho(int v);
    void trilhaEuleriana(int grauEntrada[27], int grauSaida[27]);
    bool dfs(int v);
	bool conectado();
 
 
};
 
Grafo::Grafo(int V)
{
    this->V = V;                             // atribui o número de vértices
    adj = new list<int>[V];               // cria as listas
}
 
void Grafo::adicionarAresta(int v1, int v2)
{
    adj[v1].push_back(v2);
}
 
int Grafo::devolveIndice(char letra)
{
    if (letra == 'a' or letra == 'A')
        return 0;
    else if (letra == 'b' or letra == 'B')
        return 1;
    else if (letra == 'c' or letra == 'C')
        return 2;
    else if (letra == 'd' or letra == 'D')
        return 3;
    else if (letra == 'e' or letra == 'E')
        return 4;
    else if (letra == 'f' or letra == 'F')
        return 5;
    else if (letra == 'g' or letra == 'G')
        return 6;
    else if (letra == 'h' or letra == 'H')
        return 7;
    else if (letra == 'i' or letra == 'I')
        return 8;
    else if (letra == 'j' or letra == 'J')
        return 9;
    else if (letra == 'k' or letra == 'K')
        return 10;
    else if (letra == 'l' or letra == 'L')
        return 11;
    else if (letra == 'm' or letra == 'M')
        return 12;
    else if (letra == 'n' or letra == 'N')
        return 13;
    else if (letra == 'o' or letra == 'O')
        return 14;
    else if (letra == 'p' or letra == 'P')
        return 15;
    else if (letra == 'q' or letra == 'Q')
        return 16;
    else if (letra == 'r' or letra == 'R')
        return 17;
    else if (letra == 's' or letra == 'S')
        return 18;
    else if (letra == 't' or letra == 'T')
        return 19;
    else if (letra == 'u' or letra == 'U')
        return 20;
    else if (letra == 'v' or letra == 'V')
        return 21;
    else if (letra == 'w' or letra == 'W')
        return 22;
    else if (letra == 'x' or letra == 'X')
        return 23;
    else if (letra == 'y' or letra == 'Y')
        return 24;
    else if (letra == 'z' or letra == 'Z')
        return 25;
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

bool Grafo::conectado() {
	int i, j;
	int color[26];
	queue<int> Q;
	for(i = 0; i < 26; i++) 
	{
		if (found[i] == 1)
			color[i] = 0;
		else
			color[i] = 2;
	}
	for(i=0; color[i]; i++); 
		color[i] = 1;
	Q.push(i);
	while(!Q.empty()) {
		i = Q.front(); Q.pop();
		for(j = 0; j < 26; j++) {
			if((g[i][j] || g[j][i]) && !color[j]) {
				Q.push(j);
				color[j] = 1;
			}
		}
		color[i] = 2;
	}
	for(i=0; i < 26; i++)
		if(color[i] != 2)
			return false;
	return true;
}
 

void Grafo::trilhaEuleriana(int grauEntrada[27], int grauSaida[27])
{
    int grau, val = 0;
    int vi = 0, mn = 0, ma = 0;

    if (this->conectado() == false){
        printf("The door cannot be opened.\n"); return; 
    }

    for (int i = 0; i < 26; i++)
    {
        if (grauEntrada[i] - grauSaida[i] == 1)
        	mn++;
        else if (grauSaida[i] - grauEntrada[i] == 1)
            ma++;
        else if (grauEntrada[i] != grauSaida[i]){
            printf("The door cannot be opened.\n"); return; 
        }
    }

    if(mn + ma == 0 || (mn == 1 && ma == 1)){
        printf("Ordering is possible.\n");
    } else {
    	printf("The door cannot be opened.\n"); 
    }
}
 
int main(void)
{
    int n, l, v1, v2, qtd, inicial, grauEntrada[27], grauSaida[27];
    char entrada[1001];
 
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        Grafo grafo(27);

        for (int j = 0; j < 26; j++)
        	for (int k = 0; k < 26; k++)
        		g[j][k] = 0;

        for (int j = 0; j < 27; j++)
        {
            grauEntrada[j] = 0;
            grauSaida[j] = 0;
            found[j] = 0;
        }

        scanf("%d", &l);
        for (int j = 0; j < l; j++)
        {
            scanf("%s", entrada);
            v1 = grafo.devolveIndice(entrada[0]);
            v2 = grafo.devolveIndice(entrada[strlen(entrada) - 1]);
            g[v1][v2] = 1;
            found[v1] = 1;
            found[v2] = 1;           
            grauSaida[v1] = grauSaida[v1] + 1;
            grauEntrada[v2] = grauEntrada[v2] + 1;
            
       }
 
        grafo.trilhaEuleriana(grauEntrada, grauSaida);
    }
 
    return 0;
}