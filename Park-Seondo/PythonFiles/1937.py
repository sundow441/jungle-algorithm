from sys import stdin
stdin = open("inputfile.txt", "r")

n = int(stdin.readline())

tree = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
DP = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            DP[i][j] = 1
        