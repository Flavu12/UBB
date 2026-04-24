#include <iostream>
#include <fstream>
using namespace std;
ifstream f("noduri.in");
int n, m, a[101][101];
//Determinarea matricii inchiderii tranzitive a unui graf orientat neponderat
int main()
{ f>>n>>m;
int x,y;
while(f>>x>>y)
{a[x][y]=1;}
int k, i, j;
    for(k = 1; k<=n;k++)
    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
            if(a[i][j]==0)
                a[i][j]=(a[i][k] && a[k][j]);

for(i =1;i<=n;i++)
    {for(j=1;j<=n;j++)
        cout<<a[i][j]<<" ";
    cout<<endl;
    }

return 0;
}
