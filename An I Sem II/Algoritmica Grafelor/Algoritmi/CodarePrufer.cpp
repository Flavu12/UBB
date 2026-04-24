#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

ifstream f("in.txt");
int n;
vector<int> codP;

struct nod {
	int valoare; //valoarea nodului
	int parinte; //indicele parintelui
	bool frunza = true;//indicator pentru a verifica daca nodul e frunza
	bool in_graf = true;//indicator pentru a verifica daca nodul e in graf
};

nod v[100001];

nod get_min_frunza() // cautam frunza cu valoarea cea mai mica
{
	nod aux; aux.valoare = 100001;
	for (int i = 0; i < n; i++)
		if (v[i].in_graf && v[i].frunza && i < aux.valoare)
			aux = v[i];
	return aux;
}

void codare_prufer()
{
	while (codP.size() < n - 1)
	{
		nod aux = get_min_frunza();
		codP.push_back(aux.parinte);
		v[aux.parinte].frunza = true;
		v[aux.valoare].in_graf = false;

		for (int i = 0; i < n; i++)
		{
			if (v[i].in_graf && v[i].parinte == aux.parinte)
			{
				v[aux.parinte].frunza = false;
				break;
			}
		}
	}
}


int main()
{
	f >> n;
	for (int i = 0; i < n; i++)
	{
		f >> v[i].parinte;
		v[i].valoare = i;
		if (v[i].parinte != -1)
			v[v[i].parinte].frunza = false;
		else
			v[i].frunza = false;
	}
	codare_prufer();

	cout << codP.size() << endl;

	for (int i = 0; i < codP.size(); i++)
		cout << codP[i] << " ";

	return 0;
}
