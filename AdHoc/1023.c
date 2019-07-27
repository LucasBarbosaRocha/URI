#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct cel{
    int x;
    int y;
    struct cel *prox;
}celula;

void insere(int x, int y, celula *lst);

int main(void){
int k, entrada, x, y, total_pessoas, consumo_medio, cont = 0;
float total_consumo, total;
celula *cabeca, *p;

scanf("%d^", &entrada);
while(entrada != 0){
    cont++;
    total_consumo = 0;
    total_pessoas = 0;
    cabeca = (celula *) malloc(sizeof(celula));
    cabeca -> prox = NULL;

    for(k = 0; k < entrada; k++)
    {
        scanf("%d %d", &x, &y);

        total_consumo += y;
        total_pessoas += x;
        consumo_medio = y / x;
        insere(x,consumo_medio,cabeca);
    }

    printf("Cidade# %d:\n", cont);
    p = cabeca -> prox;
    while (p != NULL)
    {
            printf("%d-%d ", p -> x, p -> y);
            p = p -> prox;
    }
    total =  total_consumo/total_pessoas;
    printf("\nConsumo medio: %.2f m3.\n\n",floor(total*100)/100);
scanf("%d", &entrada);
}

    return 0;
}

void insere(int x, int y, celula *lst)
{
    celula *nova, *p, *q;
    nova = (celula *) malloc(sizeof(celula));
    nova -> x = x;
    nova -> y = y;
    p = lst;
    q = lst -> prox;
    while(q != NULL && q -> y < nova -> y)
    {
        p = q;
        q = q -> prox;
    }

    if (q != NULL && nova -> y == q -> y) {
         q -> x = q ->x + nova -> x;
    }else{
         nova -> prox = q;
         p -> prox = nova;
    }
}
