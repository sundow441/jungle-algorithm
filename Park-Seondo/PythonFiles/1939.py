from collections import deque
from sys import stdin

stdin = open("inputfile.txt", "r")
N, M = list(map(int, stdin.readline().split()))
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, stdin.readline().strip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

target = list(map(int, stdin.readline().split()))
w = [0 for _ in range(N + 1)]

def BFS(start):
    ans = 0
    queue = deque()
    for i in graph[start]:
        queue.append(i)
    while queue:
        end, cw = queue.popleft()
        
        if w[end] < cw:
            w[end] = cw
        if ans < cw and end == target[1]:
            return cw
        for i in graph[end]:
            queue.append((i[0], i[1]))

print(BFS(target[0]))