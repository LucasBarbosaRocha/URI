/* Este programa deve ler o dia inicial de um evento, a hora, minuto e      
 * segundos iniciais, o dia em que o evento termina, hora, minuto e segundos 
 * finais. Após isso, ele deve calcular e exibir ao usuário a 
 * duração do evento na forma: W dia(s)
 *                             X hora(s)
 *                             Y minuto(s)
 *                             Z segundo(s)
 * Aluno: Rodrigo de Almeida Silva.
 * Turma: P01 – Engenharia Elétrica UFMS
 */

#include <stdio.h>

int main(){

    int diai, hi, mi, si, diaf, hf, mf, sf, h, m, s, d;
    char dia[4], lixo[2], c;

//Entrada - Dados iniciais
    scanf("%s%d", dia, &diai);
    scanf("%d%s%d%s%d", &hi, lixo, &mi, lixo, &si);

//Entrada - Dados finais
    scanf("%s%d", dia, &diaf);
    scanf("%d%s%d%s%d", &hf, lixo, &mf, lixo,  &sf);

//Se começar e terminar no mesmo dia
    if(diai == diaf){

        d = 0;

        h = hf - hi;

        if(mf < mi){

            h--;
            m = 60 + (mf - mi);
        }else if(mf >= mi){

            m = mf - mi;
        }

        if(sf < si){

            m--;
            s = 60 + (sf - si);
        }else if(sf >= si){

            s = sf - si;
        }

        if(m < 0){

            h--;    
            m = 60 + m;
        }
        if(h < 0){

            d--;
            h = 24 + h;
        }

    }else if(diai != diaf){
        
//Se durar mais que 24h.

        d = diaf - diai;

        if(hf < hi){

            d--;
            h = 24 + (hf - hi);

        }else if(hf >= hi){

            h = hf - hi;
        }

        if(mf < mi){

            h--;
            m = 60 + (mf - mi);
        }else if(mf >= mi){

            m = mf - mi;
        }

        if(sf < si){

            m--;
            s = 60 + (sf - si);
        }else if(sf >= si){

            s = sf - si;
        }

        if(m < 0){

            h--;
            m = 60 + m;
        }
        if(h < 0){

            d--;
            h = 24 + h;
        }
    }

/*Essa parte não é necessária, pois no uDebug do problema, ele trata 60 segundos como 60 segundos e não como 1 minuto, 
70 como 70 e não como 1 minuto e 10...*/

    /*while(s >= 60){

        m++;
        s = s - 60;
    }
    while(m >= 60){

        h++;
        m = m - 60;
    }
    while(h >= 24){

        d++;
        h = h - 24;
    }*/

    //Saída
    printf("%d dia(s)\n", d);
    printf("%d hora(s)\n", h);
    printf("%d minuto(s)\n", m);
    printf("%d segundo(s)\n", s);

    return 0;
}