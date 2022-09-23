import sys

sys.stdin = open('inputfile.txt','r')

N = int(input())

for i in range(9):
    print(N, " * ", i + 1, " = ", N * (i + 1))