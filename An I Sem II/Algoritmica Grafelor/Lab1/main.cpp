#include <fstream>
using namespace std;
ifstream f("graf.in");
ofstream g("graf.out");
int n,a[110][110], nod;
int main()
{ int x,y;
f>>nod;
while(f>>x)
{ f>>y;
a[x][y]=a[y][x]=1;
}
for(int i=1;i<=nod;i++)
{for(int j=1;j<=nod;j++)
    g<<a[i][j]<<" ";
    g<<'\n';
}
return 0;
}
