#include <iostream>
#include <stdio.h>
#include <list>
#include <values.h>
#include <queue>
#include <vector>
#include <stdio.h>

using namespace std;

const int INF = MAXINT/2;
#define V 501
int distancia[V];
int processado[V];
int distancia2[V];
int processado2[V];

/* Funcao que percorre um grafo e armazena em distancia o peso do menor caminho
de u para qualquer outro vertice */
void Dijkstra(int grafo[V][V], int u, int n){
    
    for(int i = 0;i <= n;i++) {
      distancia[i] = grafo[u][i];
      processado[i] = false;
    }

    distancia[u] = 0;
    processado[u] = true;
    
    while(true){ // rodar "infinitamente"
        
        int davez = -1;
        int menor = INF;
        
        // selecionamos o vértice mais próximo
        for(int i = 1;i <= n;i++)
            if(!processado[i] && distancia[i] < menor){
                davez = i;
                menor = distancia[i];
            }
        
        if(davez == -1) break; // se não achou ninguém, é o fim do algoritmo
        
        processado[davez] = true; // marcamos para não voltar para este vértice
        
        // agora, tentamos atualizar as distâncias
        for(int i = 0;i <= n;i++)
        {
            distancia[i] = min(distancia[i], distancia[davez] + grafo[davez][i]);
        }
    }
    
}

/* Funcao que percorre um grafo e armazena em distancia2 o peso do menor caminho
de u para qualquer outro vertice */
void Dijkstra2(int grafo[V][V], int u, int n){ // Verificar
    
    for(int i = 0;i <= n;i++) {
      distancia2[i] = grafo[u][i];
      processado[i] = false;
    }

    distancia2[u] = 0;
    processado2[u] = true;
    
    while(true){ // rodar "infinitamente"
        
        int davez = -1;
        int menor = INF;
        
        // selecionamos o vértice mais próximo
        for(int i = 1;i <= n;i++)
            if(!processado2[i] && distancia2[i] < menor){
                davez = i;
                menor = distancia2[i];
            }
        
        if(davez == -1) break; // se não achou ninguém, é o fim do algoritmo
        
        processado2[davez] = true; // marcamos para não voltar para este vértice
        
        // agora, tentamos atualizar as distâncias
        for(int i = 0;i <= n;i++){
          //printf("%d %d < %d\n", davez, distancia2[i], distancia2[davez] + grafo[davez][i]);
            distancia2[i] = min(distancia2[i], distancia2[davez] + grafo[davez][i]);
        } 
    }
    
}

int main()
{
  int n, m, u, v, v1, v2, peso, custoMinimo = 0;

  scanf("%d%d", &n, &m);
  while (n != 0 && m != 0)
  {
    int grafo[V][V];
    int grafoR[V][V];
    int grafoF[V][V];

    scanf("%d%d", &u, &v);

    for (int i = 0; i <= n; i++)
    {
      for (int j = 0; j <= n; j++)
      {
        grafo[i][j] = INF;
        grafoR[i][j] = INF;
        grafoF[i][j] = INF;
      }
    }

    for (int i = 0; i < m; i++)
    {
      scanf("%d%d%d", &v1, &v2, &peso);
      if (peso < grafo[v1][v2])
        grafo[v1][v2]  = peso;
      if (peso < grafo[v2][v1])
        grafoR[v2][v1] = peso;
    }



    Dijkstra(grafo, u, n);
    Dijkstra2(grafoR, v, n);

    for (int i = 0; i < n; i++)
    {
      printf("node %d\n", i);
      for (int j = 0; j < n; j++)
      {
        /* Note que essa diferenca verifica se existe um caminho que 
        ao combinar metade do caminho com a distancia do original
        com a do Reverso der o peso minimo nao deve inserir ele no grafo
        */
        if (grafo[i][j] != INF)
        {
        printf("(%d + %d + %d) != %d\n", distancia[i], grafo[i][j], distancia2[j], distancia[v]);
          if (distancia[i] + grafo[i][j] + distancia2[j] != distancia[v])
          {
            grafoF[i][j] = grafo[i][j];
          } 
        }
      }
    }


    Dijkstra(grafoF, u, n);
      if(distancia[v] > 10000)
        printf("-1\n");
      else
        printf("%d\n", distancia[v]);
    scanf("%d%d", &n, &m);
  } 
return 0;
}