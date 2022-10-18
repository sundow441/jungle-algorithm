from sys import stdin
stdin = open('inputfile.txt','r')

T = int(stdin.readline())
n = [int(stdin.readline()) for _ in range(T)]

arr = [1, 2, 3]
for i in n:
    