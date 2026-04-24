#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("in.txt");

int g[5001][5001];
int t[5001][5001];

void citesteGraf(int& v, int& e)
{
    int i, x, y, p;
    fin >> v >> e;
    for (i = 0; i < e; i++)
    {
        fin >> x >> y >> p;
        g[x][y] = p;
        g[y][x] = p;
    }
}

void algoritmPrim(int v)
{
    bool este_in_arbore[5001] = { 0 };
    // alegem nodul 0 ca radacina
    este_in_arbore[0] = 1;
    int i, j, k;
    for (i = 0; i < v - 1; i++)
    {
        int ej, ek, pondere_jk = 1001;
        // parcurgem graful (matricea de adiacenta)
        // cautam muchia cu ponderea minima cu proprietatea ca un nod al ei se afla in arbore si celalalt nod nu
        for (j = 0; j < v; j++)
        {
            for (k = 0; k < v; k++)
            {
                if (g[j][k] && este_in_arbore[j] && !este_in_arbore[k] && g[j][k] < pondere_jk)
                {
                    ej = j;
                    ek = k;
                    pondere_jk = g[j][k];
                }
            }
        }
        // se adauga in arbore nodul din afara arborelui din muchia gasita
        t[ej][ek] = pondere_jk;
        t[ek][ej] = pondere_jk;
        este_in_arbore[ek] = 1;
    }
}

int costArbore(int vt)
{
    int i, j, cost = 0;
    for (i = 0; i < vt - 1; i++)
        for (j = i + 1; j < vt; j++)
            cost += t[i][j];
    return cost;
}

void afisareMuchiiGraf(int vt)
{
    int i, j;
    for (i = 0; i < vt - 1; i++)
        for (j = i + 1; j < vt; j++) // parcurgem deasupra diag. principale pentru a afisa muchii distincte
            if (t[i][j])
                cout << i << " " << j << "\n";
}

int main()
{
    int v, e;
    citesteGraf(v, e);
    // arborele partial de cost minim contine toate nodurile din graful initial(v) si v-1 muchii
    algoritmPrim(v);
    cout << costArbore(v) << "\n";
    cout << v - 1 << "\n";
    afisareMuchiiGraf(v);
    return 0;
}