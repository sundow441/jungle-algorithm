from collections import deque
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open("inputfile.txt", "r")
M, N, H = list(map(int, stdin.readline().strip().split()))

graph = []
queue = deque([])

for i in range(H): # 상자 개수만큼 담을 tmp 생성
    tmp = []
    for j in range(N): # 상자의 y축
        tmp.append(list(map(int, stdin.readline().split())))
        for k in range(M): # 상자의 x축
            if tmp[j][k]==1:
                queue.append([i, j, k]) # 익은 토마토 좌표를 큐에 담음
    graph.append(tmp) # 상자와 토마토 그래프

directionX = [-1, 1, 0, 0, 0, 0] # 진행 방향
directionY = [0, 0, -1, 1, 0, 0]
directionZ = [0, 0, 0, 0, -1, 1]
 
days = 0
def BFS():
    global days
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            xx = x + directionX[i]
            yy = y + directionY[i]
            zz = z + directionZ[i]
            if 0 <= xx < H and 0 <= yy < N and 0 <= zz < M and graph[xx][yy][zz] == 0:
                graph[xx][yy][zz] = graph[x][y][z] + 1
                queue.append([xx, yy, zz])
    for i in graph:
        for j in i:
            for k in j:
               if k == 0:
                print(-1)
                return
            days = max(days, max(j))
    print(days-1)
BFS()