#include<stdio.h>
int main()
{
    int n, i, j, a, b, l = 1, k, p, m;
    i = j = a = b = k = p = 0;

    scanf("%d", &n);
    int M[n][n];

    while(n != 0)
    {


        for(i = 1, j = 0; i < n; i++, j++)
        {

            M[0][j] = i;

        }

        for(a = 0; a < n - 1; a++)
        {

            for(i = 1; i < n; i++)
            {

                for(j = 0, p = l + 1; p >= 1; p--, j++)
                {

                    M[i][j] = p;

                }

                for(k = 1; k < n; k++)
                {

                    M[i][j] = k;

                }

            }
        }

        for(b = n, j = 0; b > 1; b--, j++)
        {

            M[n - 1][j] = b;

        }


        for(i = 0; i < n; i++)
        {

            for(j = 0; j < n; j++)
            {

                printf("%3d", M[i][j]);

            }

        printf("\n");

        }

        scanf("%d", &n);

    }

    return 0;

}