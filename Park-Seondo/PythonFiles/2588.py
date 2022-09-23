from math import trunc
import sys

sys.stdin = open('inputfile.txt','r')

x = list(map(int, sys.stdin.read().splitlines()))

a = x[0]
b = x[1]

bHun = trunc(b/100)
bTen = trunc(b/10) - trunc(b/100)*10
bOne = b - trunc(b/10) * 10

print(a * bOne)
print(a * bTen)
print(a * bHun)
print(a * b)