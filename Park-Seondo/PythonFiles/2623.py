from collections import deque
from sys import stdin

stdin = open("inputfile.txt", "r")
N, M = list(map(int, stdin.readline().strip().split()))

graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
for _ in range(M):
    a = list(map(int, stdin.readline().strip().split()))
    for j in range(1, a[0]):
        graph[a[j]].append(a[j + 1])
        indegree[a[j + 1]] += 1

ans = []
def topologySort():
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        tmp = queue.popleft()
        ans.append(tmp)
        for i in graph[tmp]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    if len(ans) == N:
        for i in ans:
            print(i)
    else:
        print(0)

topologySort()