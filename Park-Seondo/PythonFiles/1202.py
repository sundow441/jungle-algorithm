from sys import stdin
stdin = open("inputfile.txt", "r")
N, K = list(map(int, stdin.readline().strip().split()))
J = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]
B = [int(stdin.readline()) for _ in range(K)]
J.insert(0, [0, 0])
ans = 0
for k in B:
    DP = [[0] * (k + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(1, k + 1):
            if J[i][0] > j:
                DP[i][j] = DP[i - 1][j]
            else:
                DP[i][j] = max(DP[i - 1][j], J[i][1])
    ans += DP[-1][-1]
    for m in J:
        if m[1] == DP[-1][-1]:
            m[0], m[1] = 0, 0
print(ans)