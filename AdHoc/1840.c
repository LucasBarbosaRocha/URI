#include <stdio.h>

int executaJogo(char *rodada, char *manilha);
/*0 - 3 - 6 - 9*/
int retornaValorCarta(char *carta,int isManilha);
int retornaValorNaipe(char *carta) ;
int max(int a, int b) ;
int isEmpate(int r1, int r2, int r3, int r4);
int confereResposta(int r1, int r2, int r3, int r4, int s1, int s2, int s3, int s4);

int main(void) {
int nJogadas, r1,r2,r3,r4,s1=0,s2=0,s3=0,s4=0, result, mini, resultado;
char manilha[3], p1[11], p2[11], p3[11], p4[11], rodada[12];

scanf("%d %[^\n]", &nJogadas, manilha);
scanf("%s %d", p1, &r1);
scanf("%s %d", p2, &r2);
scanf("%s %d", p3, &r3);
scanf("%s %d", p4, &r4);


while(nJogadas > 0) {
    scanf(" %[^\n]", rodada);
    result = executaJogo(rodada, manilha);
    if(result == 1)
        s1 += 1;
    else if(result == 2)
        s2 += 1;
    else if(result == 3)
        s3 += 1;
    else if(result == 4)
        s4 += 1;
    nJogadas--;
}

printf("r1 %d r2 %d r3 %d r4 %d\ns1 %d s2 %d s3 %d s4 %d ", r1, r2, r3, r4, s1, s2, s3, s4);

resultado = confereResposta(r1,r2,r3,r4,s1,s2,s3,s4);
if (resultado == 1)
    printf("%s\n",p1);
if (resultado == 2)
    printf("%s\n",p2);
if (resultado == 3)
    printf("%s\n",p3);
if (resultado == 4)
    printf("%s\n",p4);
if (resultado == 5)
    printf("*\n");
return 0;
}

int executaJogo(char *rodada, char *manilha) {
    int r1=0, r2=0, r3=0, r4=0, maxRodada,cont=0;

    if(retornaValorCarta(&rodada[0],0) == retornaValorCarta(&manilha[0],1) + 1)
        r1 = 99;
    else
        r1 = retornaValorCarta(&rodada[0],0);
    if(retornaValorCarta(&rodada[3],0) == retornaValorCarta(&manilha[0],1) + 1)
        r2 = 99;
    else
        r2 = retornaValorCarta(&rodada[3],0);
    if(retornaValorCarta(&rodada[6],0) == retornaValorCarta(&manilha[0],1) + 1)
        r3 = 99;
    else
        r3 = retornaValorCarta(&rodada[6],0);
    if(retornaValorCarta(&rodada[9],0) == retornaValorCarta(&manilha[0],1) + 1)
        r4 = 99;
    else
        r4 = retornaValorCarta(&rodada[9],0);

   maxRodada = max(max(max(r1,r2),r3),r4);

    if (maxRodada == r1)
        cont++;
    if (maxRodada == r2)
        cont++;
    if(maxRodada == r3)
        cont++;
    if(maxRodada == r4)
        cont++;

    if (cont > 1)
    {
        /*Subtrações com resultado 0, temos cartas iguais*/
        if (r1 - r2 == 0) {
            r1 += retornaValorNaipe(&rodada[1]);
            r2 += retornaValorNaipe(&rodada[4]);
        } else if(r1 - r3 == 0) {
            r1 += retornaValorNaipe(&rodada[1]);
            r3 += retornaValorNaipe(&rodada[7]);
        } else if(r1 - r4 == 0) {
            r1 += retornaValorNaipe(&rodada[1]);
            r4 += retornaValorNaipe(&rodada[10]);
        } else if(r2 - r3 == 0) {
            r2 += retornaValorNaipe(&rodada[4]);
            r3 += retornaValorNaipe(&rodada[7]);
        } else if(r2 - r4 == 0) {
            r2 += retornaValorNaipe(&rodada[4]);
            r4 += retornaValorNaipe(&rodada[10]);
        } else if(r3 - r4 == 0) {
            r3 += retornaValorNaipe(&rodada[7]);
            r4 += retornaValorNaipe(&rodada[10]);
        }
        maxRodada = max(max(max(r1,r2),r3),r4);
    }

    //printf("r1 %d r2 %d r3 %d r4 %d \n", r1, r2, r3, r4);

    if(maxRodada == r1)
        return 1;
    else if(maxRodada == r2)
        return 2;
    else if(maxRodada == r3)
        return 3;
    else if(maxRodada == r4)
        return 4;
}

int retornaValorCarta(char *carta,int isManilha) {
    if (carta[0] == '4')
        return 1;
    if (carta[0] == '5')
        return 2;
    if (carta[0] == '6')
        return 3;
    if (carta[0] == '7')
        return 4;
    if (carta[0] == 'Q')
        return 5;
    if (carta[0] == 'J')
        return 6;
    if (carta[0] == 'K')
        return 7;
    if (carta[0] == 'A')
        return 8;
    if (carta[0] == '2')
        return 9;
    if(isManilha == 0){
        if (carta[0] == '3')
            return 10;
    }else {
        return 0;
    }
}

int retornaValorNaipe(char *carta) {
    if (carta[0] == 'D')
        return 1;
    if (carta[0] == 'S')
        return 2;
    if (carta[0] == 'H')
        return 3;
    if (carta[0] == 'C')
        return 4;
}

int max(int a, int b) {
    if (a > b)
        return a;
    else
        return b;
}

int min(int a, int b){
    if (a < b)
        return a;
    else
        return b;
}

int isEmpate(int r1, int r2, int r3, int r4){
    if(r1 == r2)
        return 5;
    if(r1 == r3)
        return 5;
    if(r1 == r4)
        return 5;
    if(r2 == r3)
        return 5;
    if(r2==r4)
        return 5;
    if(r3==r4)
        return 5;
}

int confereResposta(int r1, int r2, int r3, int r4, int s1, int s2, int s3, int s4) {
    int z1=0, z2=0, z3=0, z4=0;
    /*if (r1-s1 == 0 && r1 > 0)
        z1 = 1;
    if (r2 - s2 == 0 && r2 > 0)
        z2 = 1;
    if (r3 - s4 == 0 && r3 > 0)
        z3 = 1;
    if (r4 - s4 == 0 && r4 > 0)
        z4 = 1;*/

   printf("\nz1 %d z2 %d z3 %d z4 %d\n",z1, z2, z3, z4);

    //if(z1 == 0 && z2 == 0 && z3 == 0 && z4 == 0) {
    if (r1-s1 == 0)
        z1 = 1;
    if (r2 - s2 == 0)
        z2 = 1;
    if (r3 - s3 == 0)
        z3 = 1;
    if (r4 - s4 == 0)
        z4 = 1;
    //}
   printf("z1 %d z2 %d z3 %d z4 %d\n",z1, z2, z3, z4);

    if (z1+z2+z3+z4 == 1){
        if(z1 == 1)
            return 1;
        else if (z2 == 1)
            return 2;
        else if(z3 == 1)
            return 3;
        else if(z4 == 1)
            return 4;
    }

    printf("Empate %d \n",isEmpate(r1-s1,r2-s2,r3-s3,r4-s4));
    return isEmpate(r1-s1,r2-s2,r3-s3,r4-s4);
}