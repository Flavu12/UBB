#include <iostream>
#include<fstream>
using namespace std;
ifstream f("in.txt");
int n, m, p, a[205][205], L[50000];

void Euler(int k)
{
    for (int i = 0; i < n; i++)
        if (a[k][i]) {
            a[k][i] = a[i][k] = 0;
            Euler(i);
        }
    L[++p] = k;
}
int main()
{
    int i, j;
    f >> n >> m;
    for (int K = 1; K <= m; K++) {
        f >> i >> j;
        a[i][j] = a[j][i] = 1;
    }
    Euler(0);
    for (int i = 1; i <= p; i++) cout << L[i] << " ";
    return 0;
}
