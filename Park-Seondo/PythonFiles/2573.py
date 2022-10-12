from collections import deque
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open('inputfile.txt','r')
N, M = list(map(int, stdin.readline().strip().split()))
bingsan = [list(map(int, stdin.readline().split())) for _ in range(N)]

def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    seas = []
    while queue:
        x, y = queue.popleft()
        sea = 0
        for i in range(4):
            nx = x + directionX[i]
            ny = y + directionY[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not bingsan[nx][ny]:
                    sea += 1
                elif bingsan[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seas.append((x, y, sea))
    for x, y, sea in seas:
        bingsan[x][y] = max(0, bingsan[x][y] - sea)
    return 1

iceburg = []
for i in range(N):
    for j in range(M):
        if bingsan[i][j]:
            iceburg.append((i, j))

directionX = [-1, 1, 0, 0]
directionY = [0, 0, -1, 1]
year = 0

while iceburg:
    visited = [[0] * M for _ in range(N)]
    melted = []
    group = 0
    for i, j in iceburg:
        if bingsan[i][j] and not visited[i][j]:
            group += BFS(i, j)
        if bingsan[i][j] == 0:
            melted.append((i, j))
    if group > 1:
        print(year)
        break
    iceburg = sorted(list(set(iceburg) - set(melted)))
    year += 1
for i in range(N):
    print(visited[i])
if group < 2:
    print(0)