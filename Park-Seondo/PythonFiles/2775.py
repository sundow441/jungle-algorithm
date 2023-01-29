from sys import stdin
stdin = open("inputfile.txt", "r")

T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())

    DP = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(k + 1):
        for j in range(1, n + 1):
            if i == 0:
                DP[i][j] = j
            else:
                DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
    print(DP[k][n])