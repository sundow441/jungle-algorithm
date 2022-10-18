from collections import deque
from sys import stdin

stdin = open("inputfile.txt", "r")
n = int(stdin.readline().strip())
m = int(stdin.readline().strip())

graph = [[] * (n + 1) for _ in range(n + 1)]
reverseGraph = [[] * (n + 1) for _ in range(n + 1)]
indegree = [0] * (n + 1)
result = [0] * (n + 1)
check = [0] * (n + 1)
queue = deque()
for _ in range(m):
    a, b, c = map(int, stdin.readline().strip().split())
    graph[a].append((b, c))
    reverseGraph[b].append((a, c))
    indegree[b] += 1

start, end = map(int, stdin.readline().strip().split())
queue.append(start)

def topologySort():
    while queue:
        cur = queue.popleft()
        for i, c in graph[cur]:
            indegree[i] -= 1
            result[i] = max(result[i], result[cur] + c)
            if indegree[i] == 0:
                queue.append(i)

    # 백트래킹
    cnt = 0
    queue.append(end)
    while queue:
        cur = queue.popleft()
        for i, c in reverseGraph[cur]:
            if result[cur] - result[i] == c:
                cnt += 1
                if check[i] == 0:
                    queue.append(i)
                    check[i] = 1
    print(result[end])
    print(cnt)

topologySort()