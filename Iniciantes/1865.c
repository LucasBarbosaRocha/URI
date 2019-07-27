#include <stdio.h>
#include <string.h>

int main(void) {
	int casos, forca;
	char nome[16], t[] = "Thor";

	scanf("%d",&casos);

	while(casos > 0) {

		scanf("%s", &nome);
		scanf("%d", &forca);

		if(strcmp(nome,t) == 0)
			printf("Y\n");
		else
			printf("N\n");
		casos--;
	}
return 0;
}