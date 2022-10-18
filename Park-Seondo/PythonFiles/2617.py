from sys import stdin

stdin = open("inputfile.txt", "r")
N, M = list(map(int, stdin.readline().strip().split()))

bigger = [[] for _ in range(N + 1)]
smaller = [[] for _ in range(N + 1)]
mid = (N + 1) // 2

for i in range(M):
    a, b = map(int, stdin.readline().strip().split())
    bigger[b].append(a)
    smaller[a].append(b)


def DFS(arr, start):
    global count
    for i in arr[start]:
        if not visited[i]:
            visited[i] = 1
            count += 1
            DFS(arr, i)

ans = 0
for i in range(1, N + 1):
    visited = [0 for _ in range(N + 1)]
    count = 0
    DFS(smaller, i)
    if count >= mid:
        ans +=1
    count = 0
    DFS(bigger, i)
    if count >= mid:
        ans +=1
print(ans)