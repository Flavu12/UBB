#include<iostream>
#include<fstream>
#include<queue>

using namespace std;

ifstream f("in.txt");

int n, nod, nr_aparitii[10001], nod_disponibil, parinte[10001];
queue<int> cod;

int main()
{
	f >> n;
	for (int i = 0; i < n; i++)
	{
		f >> nod;
		cod.push(nod);
		nr_aparitii[nod]++;
		parinte[i] = -1;
	}

	parinte[n] = -1;
	for (int i = 1; i <= n; i++)
	{
		nod = cod.front();
		nod_disponibil = 0;
		while (nr_aparitii[nod_disponibil] != 0)
			nod_disponibil++;
		parinte[nod_disponibil] = nod;
		cod.pop();
		cod.push(nod_disponibil);
		nr_aparitii[nod_disponibil]++;
		nr_aparitii[nod]--;
	}
	cout << n + 1 << endl;
	for (int i = 0; i <= n; i++)
		cout << parinte[i] << " ";

	return 0;

}