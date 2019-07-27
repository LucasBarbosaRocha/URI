#include <stdio.h>
#include <string.h>

int main(void)
{
    int n, tam, i, j;
    char s[101], r[101], r2[101];

    scanf("%d", &n);
    getchar();
    while(n-- > 0)
    {
        scanf("%[^\n]", s);
        getchar();
        tam = strlen(s);
        j=0;
        for(i = (tam/2)-1; i>= 0; i--,j++)
            r[j] = s[i];
        j=0;
        for(i=tam-1; i>= (tam/2); i--,j++)
            r2[j] = s[i];
        r[tam/2] = '\0';
        r2[tam/2] = '\0';

        printf("%s%s\n",r, r2);
        
    }
return 0;
}