from collections import deque
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open("inputfile.txt", "r")
n = int(stdin.readline())

room = [list(map(int, stdin.readline().strip())) for _ in range(n)]

def BFS(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + directionX[i]
            yy = y + directionY[i]
            if 0 <= xx < n and 0 <= yy < n:
                if visited[xx][yy] == -1:
                    if room[xx][yy] == 0:
                        queue.append([xx, yy])
                        visited[xx][yy] = visited[x][y] + 1
                    else:
                        queue.appendleft([xx, yy])
                        visited[xx][yy] = visited[x][y]

visited = [[-1] * n for _ in range(n)]

directionX = [-1, 1, 0, 0]
directionY = [0, 0, -1, 1]

BFS(0, 0)
print(visited[n - 1][n - 1])