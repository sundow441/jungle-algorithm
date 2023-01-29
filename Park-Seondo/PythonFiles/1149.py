from sys import stdin
stdin = open("inputfile.txt", "r")
N = int(stdin.readline())
house = [list(map(int, stdin.readline().split())) for _ in range(N)]
arr = []
ans = 0

for i in range(N):
    tmp = 1001
    arr.append(1001)
    for j in range(3):
        if i == 0 and min(house[i]) == house[i][j]:
            arr[-1] = j
            break
        elif i != 0:
            if arr[-2] == j:
                continue
            elif tmp > house[i][j]:
                tmp = house[i][j]
                arr[-1] = j
print(arr)
for k in range(N):
    ans += house[k][arr[k]]
print(ans)
                