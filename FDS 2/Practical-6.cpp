#include <iostream>
#include <stdlib.h>
using namespace std;

int cost[10][10], i, j, k, n, qu[10], front = 0, rear = 0, v, visit[10] = {0}, visited[10] = {0};
// Initialized all elements of visit and visited arrays to 0

int stk[10], top = -1, visit1[10] = {0}, visited1[10] = {0};
// Initialized all elements of visit1 and visited1 arrays to 0 and top to -1

void bfs(int v)
{
    qu[rear++] = v;
    visit[v] = 1;
    while (front != rear)
    {
        v = qu[front++];
        cout << v << " ";
        for (j = 1; j <= n; j++)
        {
            if (cost[v][j] != 0 && visit[j] == 0 && visited[j] == 0)
            {
                qu[rear++] = j;
                visit[j] = 1;
            }
        }
        visited[v] = 1;
    }
}

void dfs(int v)
{
    stk[++top] = v;
    visit1[v] = 1;
    while (top != -1)
    {
        v = stk[top--];
        cout << v << " ";
        visited1[v] = 1;
        for (j = n; j >= 1; j--)
        {
            if (cost[v][j] != 0 && visit1[j] == 0 && visited1[j] == 0)
            {
                stk[++top] = j;
                visit1[j] = 1;
            }
        }
    }
}

int main()
{
    int m;
    cout << "Enter number of vertices : ";
    cin >> n;
    cout << "Enter number of edges : ";
    cin >> m;

    cout << "\nEDGES :\n";
    for (k = 1; k <= m; k++)
    {
        cin >> i >> j;
        cost[i][j] = 1;
        cost[j][i] = 1;
    }

    // display function
    cout << "The adjacency matrix of the graph is : " << endl;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            cout << " " << cost[i][j];
        }
        cout << endl;
    }

    cout << "Enter initial vertex for BFS: ";
    cin >> v;
    cout << "The BFS of the Graph is: ";
    bfs(v);

    cout << endl
         << "Enter initial vertex for DFS: ";
    cin >> v;
    cout << "The DFS of the Graph is: ";
    dfs(v);

    return 0;
}
