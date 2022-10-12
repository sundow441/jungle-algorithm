from collections import deque
from sys import stdin

stdin = open("inputfile.txt", "r")
N = int(stdin.readline().strip())
M = int(stdin.readline().strip())

graph = [[] for _ in range(N + 1)]
chasu = [0 for _ in range(N + 1)]
bupum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, stdin.readline().strip().split())
    graph[b].append((a, c))
    chasu[a] += 1

def topologySort():
    queue = deque()
    for i in range(1, N + 1):
        if chasu[i] == 0 :
            queue.append(i)
    while queue:
        tmp = queue.popleft()
        for i in graph[tmp]:
            if bupum[tmp].count(0) == N + 1:
                bupum[i[0]][tmp] += i[1]
            else:
                for j in range(1, N + 1):
                    bupum[i[0]][j] += bupum[tmp][j] * i[1]
            chasu[i[0]] -= 1
            if chasu[i[0]] == 0:
                queue.append(i[0])
        
        for i in bupum:
            print(i)
        print()
    for i in enumerate(bupum[N]):
        if i[1] > 0:
            print(*i)

topologySort()
