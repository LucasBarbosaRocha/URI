#include<stdio.h>
#define MAX 51
int main (void)
{
    char M[MAX], lixo, c=0;
    int i, j, b, y, tam, a;
    scanf("%d", &b);
    scanf("%c", &lixo);
    for(i=0; i<b; i++)
    {
        scanf("%s", M);
        scanf(" %d", &a);

        for(j=0; M[j] != '\0'; j++)
        {
                c=M[j]-a;
                if(c < 65)
                {
                    c=(M[j]-a)+26;
                }
                else
                {
                    c=M[j]-a;
                }

            printf("%c", c);

        }
        printf("\n");

    }
    return 0;
}