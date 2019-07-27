#include <stdio.h>

void subtrair(int n1, int d1, int n2, int d2);
void somar(int n1, int d1, int n2, int d2);
void multiplicar(int n1, int d1, int n2, int d2);
void dividir(int n1, int d1, int n2, int d2);
void imprimir(int n, int d, int sn, int sd);
int mdc(int n, int d);

int main(void)
{
	int n, n1, d1, n2, d2;
	char s, s1, s2;

	scanf("%d", &n);

	while (n-- > 0)
	{
		scanf("%d %c %d %c %d %c %d", &n1, &s1, &d1, &s, &n2, &s2, &d2);
		//printf("%d%c%d%c%d%c%d\n", n1,s1,d1,s,n2,s2,d2);
		if (s == '-')
			subtrair(n1, d1, n2, d2);
		else if(s == '+')
			somar(n1, d1, n2, d2);
		else if(s == '/')
			dividir(n1, d1, n2, d2);
		else if(s == '*')
			multiplicar(n1, d1, n2, d2);
	}
	return 0;
}

void subtrair(int n1, int d1, int n2, int d2)
{
	int n, d, sn, sd, md, auxN, auxD;
	n = (n1*d2)-(n2*d1);
	d = d1*d2;
	if (n < 0) auxN = n*(-1);
	else auxN = n;
	if (d < 0) auxD = d*(-1);
	else auxD = d;
	md = mdc(auxN, auxD);
	sn = n / md;
	sd = d / md;
	imprimir(n, d, sn, sd);
}

void somar(int n1, int d1, int n2, int d2)
{	
	int n, d, sn, sd, md, auxN, auxD;
	n = (n1*d2)+(n2*d1);
	d = d1*d2;
	if (n < 0) auxN = n*(-1);
	else auxN = n;
	if (d < 0) auxD = d*(-1);
	else auxD = d;
	md = mdc(n, d);
	sn = n / md;
	sd = d / md;
	imprimir(n, d, sn, sd);
}

void multiplicar(int n1, int d1, int n2, int d2)
{
	int n, d, sn, sd, md, auxN, auxD;
	n = n1*n2;
	d = d1*d2;
	if (n < 0) auxN = n*(-1);
	else auxN = n;
	if (d < 0) auxD = d*(-1);
	else auxD = d;
	md = mdc(n, d);
	sn = n / md;
	sd = d / md;
	imprimir(n, d, sn, sd);
}

void dividir(int n1, int d1, int n2, int d2)
{
	int n, d, sn, sd, md, auxN, auxD;
	n = n1*d2;
	d = d1*n2;
	if (n < 0) auxN = n*(-1);
	else auxN = n;
	if (d < 0) auxD = d*(-1);
	else auxD = d;
	md = mdc(n, d);
	sn = n / md;
	sd = d / md;
	imprimir(n, d, sn, sd);
}

void imprimir(int n, int d, int sn, int sd)
{
	printf("%d/%d = %d/%d\n", n, d, sn, sd);
}

int mdc(int n, int d)
{
	int resto;
	resto = n % d;
	while (resto != 0)
	{
		n = d;
		d = resto;
		resto = n % d;
	}
	return d;
}