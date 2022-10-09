from math import inf
from math import sqrt
from sys import stdin

stdin = open('inputfile.txt', 'r')
n = int(stdin.readline())
a = []
for _ in range(n):
    a.append(list(map(int, stdin.readline().split())))
a.sort()

arr = []
def distance(a1, a2):
    return (a1[0] - a2[0])**2 + (a1[1] - a2[1])**2

def dujeom(pl, pr):
    if pl == pr:
        return float(inf)
    if pr - pl == 1:
        return distance(a[pl], a[pr])
    
    pc = (pl + pr) // 2
    smallDist = min(dujeom(pl, pc), dujeom(pc, pr))

    target = []
    for i in range(pl, pr + 1):
        if (a[pc][0] - a[i][0])**2 < smallDist:
            target.append(a[i])

    target.sort(key=lambda x: x[1])

    t = len(target)
    for i in range(t-1):
        for j in range(i+1, t):
            if (target[i][1] - target[j][1])**2 < smallDist:
                smallDist = min(smallDist, distance(target[i],target[j]))
            else:
                break
    return smallDist
print(int(dujeom(0, n - 1)))