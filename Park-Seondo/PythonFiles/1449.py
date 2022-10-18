from sys import stdin
stdin = open("inputfile.txt", "r")

N, L = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))
arr.sort()
count = 1
tmp = 0

for i in range(1, N):
    if arr[i] - arr[tmp] <= (L - 1):
        pass
    elif arr[i] - arr[tmp] > (L - 1):
        tmp = i
        count += 1
print(count)