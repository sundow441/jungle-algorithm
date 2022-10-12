from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open('inputfile.txt','r')
N = int(stdin.readline())
A = list(map(int, stdin.readline().strip().split()))
M = list(map(int, stdin.readline().strip().split()))

Max = -1000000000
Min = 1000000000

def DFS(n, ans, plus, minus, multiplication, division):
    global Max
    global Min
    if n == N:
        Max = max(ans, Max)
        Min = min(ans, Min)
        return
    
    if plus:
        DFS(n + 1, ans + A[n], plus - 1, minus, multiplication, division)
    if minus:
        DFS(n + 1, ans - A[n], plus, minus - 1, multiplication, division)
    if multiplication:
        DFS(n + 1, ans * A[n], plus, minus, multiplication - 1, division)
    if division:
        DFS(n + 1, int(ans / A[n]), plus, minus, multiplication, division - 1)

DFS(1, A[0], M[0], M[1], M[2], M[3])
print(Max)
print(Min)