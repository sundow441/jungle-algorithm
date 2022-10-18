from sys import stdin
stdin = open("inputfile.txt", "r")
N, K = list(map(int, stdin.readline().strip().split()))

arr = [[0, 0]]
for _ in range(N):
    arr.append(list(map(int, stdin.readline().split())))

LCS = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j < arr[i][0]:
            LCS[i][j] = LCS[i - 1][j]
        else:
            LCS[i][j] = max(arr[i][1] + LCS[i- 1][j - arr[i][0]], LCS[i - 1][j])

print(LCS[N][K])