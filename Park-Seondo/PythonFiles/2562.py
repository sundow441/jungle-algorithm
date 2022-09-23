import sys

sys.stdin = open('inputfile.txt','r')
n = list(map(int, sys.stdin.read().splitlines()))

print(max(n))
print(n.index(max(n))+1)