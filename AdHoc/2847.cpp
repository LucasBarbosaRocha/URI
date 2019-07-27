#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;
typedef long long ll;

int main(int argc, char** argv)
{
	string entrada;
	getline(cin,entrada);

	int I=0,l=0,o=0,v=0,e=0,y=0,u=0,sim=0;

	for (int i = 0; i < entrada.length(); i++)
	{
		if (entrada[i] == 'I')
			I = I + 1;
		if (entrada[i] == 'l')
			l = l + 1;
		if (entrada[i] == 'o')
			o = o + 1;
		if (entrada[i] == 'v')
			v = v + 1;
		if (entrada[i] == 'e')
			e = e + 1;
		if (entrada[i] == 'y')
			y = y + 1;
		if (entrada[i] == 'u')
			u = u + 1;
		if (entrada[i] == '!')
			sim = sim + 1;
	}

	int qtd = 0;
	while (I > 0 && l > 0 && o > 0 && v > 0 && e > 0 && y > 0 && u > 0 && sim > 0)
	{	
		qtd++;
		I--; l--; o-=2;v--;e--;y--;u--;sim--;
	}
	cout<<qtd<<endl;
	return 0;
}