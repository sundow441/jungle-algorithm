from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open('inputfile.txt','r')
N = int(stdin.readline())
A = list(map(int, stdin.readline().strip().split()))
M = list(map(int, stdin.readline().strip().split()))
print(M)