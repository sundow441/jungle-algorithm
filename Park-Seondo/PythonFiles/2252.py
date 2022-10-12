from collections import deque
from sys import stdin

stdin = open("inputfile.txt", "r")
N, M = list(map(int, stdin.readline().strip().split()))
heightCompare = [list(map(int, stdin.readline().strip().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
students = [0] * (N + 1)
for i in range(M):
    graph[heightCompare[i][0]].append(heightCompare[i][1])
    students[heightCompare[i][1]] += 1

ans = []
def topologySort():
    queue = deque()
    for i in range(1, N + 1):
        if students[i] == 0:
            queue.append(i)

    while queue:
        tmp = queue.popleft()
        ans.append(tmp)
        for i in graph[tmp]:
            students[i] -= 1
            if students[i] == 0:
                queue.append(i)
    return ans
print(*topologySort())