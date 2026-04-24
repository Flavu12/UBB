/*
Algoritmul lui Moore
Cel mai scurt drum de la nodul sursa la toate celelalte noduri accesibile
*/
#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;
#define INFINITY 9999
#define max 300
int main() {
    int G[max][max];
    ifstream f("input.txt");
    ofstream g("output.txt");
    int m, n, s, x, y;
    f >> m >> n >> s;//m=nr noduri, n=nr muchii, s=nod sursa
    for (int i = 0; i < max; i++)
        for (int j = 0; j < max; j++)
            G[i][j] = 0;
    for (int i = 1; i <= n; i++)
    {
        f >> x >> y;
        G[x][y] = 1;
    }
    int startnode = s;
    int cost[max][max], distance[max], pred[max];
    int visited[max], count, mindistance, nextnode = 0, i, j;
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            if (G[i][j] == 0)
                cost[i][j] = INFINITY;
            else
                cost[i][j] = G[i][j];
    for (i = 0; i < n; i++) {
        distance[i] = cost[startnode][i];
        pred[i] = startnode;
        visited[i] = 0;
    }
    distance[startnode] = 0;
    visited[startnode] = 1;
    count = 1;
    while (count < n - 1) {
        mindistance = INFINITY;
        for (i = 0; i < n; i++)
            if (distance[i] < mindistance && !visited[i]) {
                mindistance = distance[i];
                nextnode = i;
            }
        visited[nextnode] = 1;
        for (i = 0; i < n; i++)
            if (!visited[i])
                if (mindistance + cost[nextnode][i] < distance[i])
                {
                    distance[i] = mindistance + cost[nextnode][i];
                    pred[i] = nextnode;
                }
        count++;
    }
    int v[max];
    int k;
    for (i = 0; i < n; i++)
        if (i != startnode && distance[i] < max) {
            k = 0;
            g << distance[i] + 1 << " ";
            v[k++] = i;
            j = i;
            do {
                j = pred[j];
                v[k++] = j;
            } while (j != startnode);
            for (int j = k - 1; j >= 0; --j)
            {
                g << v[j] << " ";
            }
            g<< endl;
        }
        else if (distance[i] < max) { g << 1 << " " << startnode << " "<<endl; }
    return 0;
}
