from collections import deque
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open("inputfile.txt", "r")

count = 1
def BFS(x, y):
    global count
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + directionX[i]
            yy = y + directionY[i]
            if 0 <= xx < N and 0 <= yy < M:
                if graph[xx][yy] == 0:
                    continue
                elif graph[xx][yy] == 1:
                    graph[xx][yy] = graph[x][y] + 1
                    queue.append((xx, yy))
                    count += 1
            else:
                continue
    return graph[N-1][M - 1]

N, M = list(map(int, stdin.readline().strip().split()))

graph = [list(map(int, stdin.readline().strip())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
coordinates = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            coordinates.append((i, j))

directionX = [-1, 1, 0, 0]
directionY = [0, 0, -1, 1]

print(BFS(0, 0))