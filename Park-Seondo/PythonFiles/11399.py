from sys import stdin
stdin = open("inputfile.txt", "r")
N = int(stdin.readline())

arr = list(map(int, stdin.readline().split()))
arr.sort()
for i in range(1, len(arr)):
    arr[i] += arr[i - 1]
print(sum(arr))