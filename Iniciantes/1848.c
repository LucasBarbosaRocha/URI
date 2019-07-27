#include <stdio.h>
#include <string.h>

int length(char v[7]){
	int i = 0, cont = 0;

	while(v[i]!='\0'){
		cont++;
		i++;
	}

	return cont;
}

int myStrcmp(char v1[7], char v2[7]){
	int i = 0;

	if(length(v1) != length(v2))
		return 1;


	while(v1[i]==v2[i]){
		i++;
		if(v1[i]!=v2[i]) 
			return 0;
	}
	return 1;
}

int main(void) {
	int n = 3, aux;
	char entrada[7], tmp[3], cont, palavra[7];
	strcpy(palavra,"caw caw");
	/* Verificando o sonho */

	while (n-- > 0) {
		cont = 0;
		do{
			scanf(" %[^\n]", entrada);
			/*gets(entrada);*/

			aux = myStrcmp(entrada,palavra);

			if(aux!=0){
				strcpy(tmp,entrada);

				if(tmp[0]=='*')
					cont += 4;
				if(tmp[1]=='*')
					cont += 2;
				if(tmp[2]=='*')
					cont += 1;

			}

		}while(aux != 0);

		printf("%d\n", cont);
	}


return 0;
}