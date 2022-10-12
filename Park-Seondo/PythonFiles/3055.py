from collections import deque
from sys import stdin

stdin = open("inputfile.txt", "r")
R, C = list(map(int, stdin.readline().strip().split()))

graph = [list(stdin.readline().strip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

queue = deque([])
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            queue.append((i, j))
        elif graph[i][j] == 'D':
            Dx, Dy = i, j

for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            queue.append((i, j))

def BFS(dx, dy):
    while queue:
        x, y = queue.popleft()
        if graph[Dx][Dy] == 'S':
            return visited[dx][dy]
        for i in range(4):
            xx = x + directionX[i]
            yy = y + directionY[i]
            if graph[x][y] == 'S' and 0 <= xx < R and 0 <= yy < C and (graph[xx][yy] == '.' or graph[xx][yy] == 'D'):
                queue.append((xx, yy))
                visited[xx][yy] = visited[x][y] + 1
                graph[xx][yy] = 'S'
            if graph[x][y] == '*' and 0 <= xx < R and 0 <= yy < C and (graph[xx][yy] == '.' or graph[xx][yy] == 'S'):
                queue.append((xx, yy))
                graph[xx][yy] = '*'
    return 'KAKTUS'

directionX = [-1, 1, 0, 0]
directionY = [0, 0, -1, 1]
print(BFS(Dx, Dy))