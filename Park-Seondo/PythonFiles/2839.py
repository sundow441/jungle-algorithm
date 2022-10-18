from sys import stdin
stdin = open("inputfile.txt", "r")

N = int(stdin.readline())

arr = [-1] * 5001
arr[3] = arr[5] = 1

for i in range(6, N + 1):
    if i % 5 == 0:
        arr[i] = arr[i - 5] + 1
    elif i % 3 == 0:
        arr[i] = arr[i - 3] + 1
    elif i % 5 != 0 and i % 3 != 0:
        arr[i] = min(arr[i - 5], arr[i - 3])
print(max(arr))