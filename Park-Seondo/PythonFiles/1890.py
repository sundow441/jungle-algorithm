from collections import deque
from sys import stdin
stdin = open("inputfile.txt", "r")

N = int(stdin.readline())
arr = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]

target = deque()
ans = 0
def a():
    target.append((0, 0 + arr[0][0]))
    target.append((0 + arr[0][0], 0))
    while target:
        for i in range(N):
            for j in range(N):
                if target[0][0] == i and target[0][1] == j:
                    DP[i][j] += 1
                    print(i, j, DP[i][j])
                    print(arr[i][j])
                    if i + arr[i][j] < N and j + arr[i][j] < N:
                        target.append((i, j + arr[i][j]))
                        target.append((i + arr[i][j], j))
                        if (i == (N - 1) and (j + arr[i][j]) == (N - 1)) or ((j + arr[i][j]) == (N - 1) and j == N - 1):
                            ans += 1
                        target.popleft()
                        print(target)
                    else:
                        target.popleft()
                    
a()
print(ans)