import sys

sys.stdin = open('inputfile.txt','r')
a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
c, d = divmod(a, b)
print(c)
print(d)