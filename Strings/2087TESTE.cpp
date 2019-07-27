#include <iostream>
#include <set>
#include <string>
using namespace std;

int main() 
{
	int n;
	string anterior, atual;
	cin >> n;
	while (n != 0)
	{
		set<string> seq;
		for (int i = 0; i < n; i++)
		{
			cin >> atual;
			if (anterior.find(atual) + 1)
			{
                seq.insert(anterior);
                seq.insert(atual);
            }
            anterior.swap(atual);			
		}
        cout << seq.size() << endl;
		cin >> n;
	}

	return 0;
}