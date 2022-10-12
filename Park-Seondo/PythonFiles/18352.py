from collections import deque
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open("inputfile.txt", "r")

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
N, M, K, X = list(map(int, stdin.readline().strip().split()))

graph = [[] for _ in range(N + 1)]
distance = [0] * (N + 1)
for i in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

visited = [0 for _ in range(N + 1)]

def BFS(V):
    global distance
    distance[V] = 0
    queue = deque([V])
    ans = []
    visited[V] = 1
    while queue:
        V = queue.popleft()
        for i in graph[V]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                distance[i] = distance[V] + 1
                if distance[i] == K:
                    ans.append(i)
    if len(ans) == 0:
        print(-1)
    else:
        ans.sort()
        for i in ans:
            print(i)
BFS(X)