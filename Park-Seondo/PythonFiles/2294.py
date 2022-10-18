from sys import stdin

stdin = open("inputfile.txt", "r")
n, k = list(map(int, stdin.readline().strip().split()))
coins = [int(stdin.readline().strip()) for _ in range(n)]

smallest = [10**5] * (k + 1)
smallest[0] = 0

for i in coins:
    for j in range(i, k + 1):
        smallest[j] = min(smallest[j], smallest[j - i] + 1)

if smallest[k] == 10**5:
    print(-1)
else:
    print(smallest[k])