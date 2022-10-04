from sys import stdin

stdin = open('inputfile.txt', 'r')
n = stdin.read().splitlines()
Q = list(map(int, n[0].split()))
ans = 1

def gobsem(a, b, c):
    global ans
    if b == 1:
        ans = a % c
        return ans
    else:
        ans = gobsem(a, b // 2, c)
        if b % 2 == 0:
            return (ans * ans) % c
        else:
            return (ans * ans * a) % c

print(gobsem(Q[0], Q[1], Q[2]))