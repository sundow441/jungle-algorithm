from collections import deque
from sys import stdin

stdin = open("inputfile.txt", "r")

def BFS():
    time = 0
    queue = deque(virusInfo)

    while queue:
        if time == S or graph[X - 1][Y - 1] != 0:
            break
        for _ in range(len(queue)):
            virus, x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = virus
                        queue.append((graph[nx][ny], nx, ny))
        time += 1
    return graph[X - 1][Y - 1]

N, K = list(map(int, stdin.readline().strip().split()))
graph = []
virusInfo = []
for i in range(N):
    graph.append(list(map(int, stdin.readline().strip().split())))
    for j in range(N):
        if graph[i][j] != 0:
            virusInfo.append((graph[i][j], i, j))

S, X, Y = list(map(int, stdin.readline().split()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

virusInfo.sort()
print(BFS())            