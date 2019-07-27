#include <stdio.h>

int main(void)
{
    int n, k, i, dif, resul;
    char c[51];

    scanf("%d", &n);

    while(n-- > 0)
    {

        scanf("%s", c);
        scanf(" %d", &k);

        for(i = 0; c[i] != '\0'; i++)
        {
            resul = k;
            if(c[i]-k < 65)
            {
                dif = (c[i]-65)+1;
                resul = k - dif;
                printf("%c", 90-resul);

            }else
            printf("%c", c[i]-resul);
    
        }
        printf("\n");
    }
    return 0;
}