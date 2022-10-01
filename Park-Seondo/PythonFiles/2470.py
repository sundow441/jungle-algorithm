from sys import stdin

stdin = open('inputfile.txt', 'r')
n = stdin.read().splitlines()
N = int(n[0])
n.remove(n[0])
n = sorted(list(map(int, n[0].split())))

def Binary(arr, pl, pr):
    summ = 2000000000
    while pl < pr:
        if abs(arr[pl] + arr[pr]) <= summ:
            ans[0] = arr[pl]
            ans[1] = arr[pr]
            summ = abs(arr[pl] + arr[pr])
        if arr[pl] + arr[pr] < 0:
            pl += 1
        elif arr[pl] + arr[pr] >= 0:
            pr -= 1
    print(*sorted(ans))

ans = [0, 0]
pl = 0
pr = len(n) - 1

Binary(n, pl, pr)