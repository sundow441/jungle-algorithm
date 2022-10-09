from sys import stdin

stdin = open('inputfile.txt','r')
N, M, V = list(map(int, stdin.readline().split()))

graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, stdin.readline().strip().split())
    graph[a][b] = graph[b][a] = 1
visited = [0] * (N+1)
visited2 = [0] * (N+1)
def DFS(V):
    visited[V] = 1
    print(V, end=" ")
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited[i] == 0:
            DFS(i)
DFS(V)
print()

def BFS(V):
    queue = [V]
    visited2[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end=" ")
        for i in range(1, N+1):
            if visited2[i] == 0 and graph[V][i] == 1:
                queue.append(i)
                visited2[i] = 1
BFS(V)