from sys import stdin

stdin = open("inputfile.txt", "r")
n, k = list(map(int, stdin.readline().strip().split()))
coins = [int(stdin.readline().strip()) for _ in range(n)]
print(coins)
