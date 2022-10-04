from math import sqrt
from sys import stdin

stdin = open('inputfile.txt', 'r')
n = int(stdin.readline())
a = []
for _ in range(n):
    a.append(list(map(int, stdin.readline().split())))
a.sort()
print(a)

def dujeom():
    k = 10000
    for i in range(n):
        l = sqrt(((abs(a[i][0] - a[i - 1][0]))**2) + ((abs(a[i][1] - a[i - 1][1]))**2))
        if k > l:
            k = l
    print(int(k) ** 2)
dujeom()