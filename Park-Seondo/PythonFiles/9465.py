from sys import stdin
stdin = open("inputfile.txt", "r")

T = int(stdin.readline())
for _ in range(T):
    n = []
    arr = []
    n.append(stdin.readline())
    for _ in range(2):
        arr.append(list(map(int, stdin.readline().split())))
    for i in range(1, len(arr[0])):
        if i == 1:
            arr[0][i] += arr[1][i - 1]
            arr[1][i] += arr[0][i - 1]
        else:
            arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
            arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])
    print(max(arr[0][-1], arr[1][-1]))