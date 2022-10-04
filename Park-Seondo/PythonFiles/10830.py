from random import randrange
from sys import stdin

stdin = open('inputfile.txt', 'r')
N, B = map(int, stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, stdin.readline().split())))


def hengryeol(a, b):
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += a[i][k] * b[k][j]
            arr[i][j] = tmp % 1000
    return arr

def jisu(a, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    else:
        ans = jisu(a, b // 2)
        if b % 2 == 0:
            return hengryeol(ans, ans)
        else:
            return hengryeol(hengryeol(ans, ans), a)
ans = jisu(A, B)
for i in ans:
    print(*i)