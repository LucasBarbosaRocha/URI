#include <stdio.h>

int main(void)
{
	char lixo[4], lixo2[2];
	int hi, mi, si, hf, mf, sf, di, df;
	long int durI, durF, dur;

	scanf("%s%d", lixo, &di);
	scanf("%d%s%d%s%d", &hi,lixo2, &mi, lixo2, &si);
	scanf("%s%d", lixo, &df);
	scanf("%d%s%d%s%d", &hf, lixo2, &mf, lixo2, &sf);

	durI = ((di*86400) + (hi*3600) + (mi*60) + si);
	durF = ((df*86400) + (hf*3600) + (mf*60) + sf);
	dur = durF - durI;

	printf("%ld dia(s)\n", ((dur/86400)));
	printf("%ld hora(s)\n", (((dur%86400)/3600)));
	printf("%ld minuto(s)\n", ((((dur%86400)%3600)/60)));
	printf("%ld segundo(s)\n", (((((dur%86400)%3600)%60))));
	return 0;
}