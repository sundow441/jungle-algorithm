from sys import stdin

stdin = open("inputfile.txt", "r")
N, K = list(map(int, stdin.readline().strip().split()))

coins = [int(stdin.readline()) for _ in range(N)]
coins.sort()
ans = 0
for i in range(N - 1, -1, -1):
    ans += (K // coins[i])
    K %= coins[i]
print(ans)