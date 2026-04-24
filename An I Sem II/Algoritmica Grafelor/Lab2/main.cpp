#include <iostream>
#include <fstream>
using namespace std;
ifstream f("graf.in");
ofstream g("graf.out");
int n,a[110][110];
int grad(int x)
{int g=0;
for(int j=1;j<=n;j++)
g+=a[x][j];
return g;
}
int main()
{ f>>n;
int x,y;
while(f>>x)
{ f>>y;
a[x][y]=a[y][x]=1;
}
//Pentru noduri izolate
g<<"Nodurile izolate sunt: ";
for(int i=1;i<=n;i++)
    if(grad(i)==0)
   g<<i<<" ";
g<<endl;
//Pentru graf regular
int ok =1;
for(int i=1;i<n;i++)
    for(int j=i+1;j<=n;j++)
        if(grad(i)!=grad(j))
            ok=0;
if(ok==0)
g<<"Graful nu este regulat";
else g<<"Graful este regulat!";
return 0;
}
