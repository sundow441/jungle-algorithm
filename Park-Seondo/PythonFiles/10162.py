from sys import stdin
stdin = open("inputfile.txt", "r")
T = int(stdin.readline())
tmp = [0, 0, 0]

while T > 0:
    if T >= 300:
        tmp[0] = T // 300
        T %= 300
    if T >= 60:
        tmp[1] = T // 60
        T %= 60
    if T % 10 == 0:
        tmp[2] = T // 10
        T %= 10
    else:
        print(-1)
        break
    print(*tmp)