import sys

sys.stdin = open('inputfile.txt', 'r')
n = sys.stdin.read().splitlines()
N = int(n[0]) # 제공되는 정수의 개수
A = sorted(list(map(int, n[1].split()))) #제공되는 정수들
M = int(n[2]) # 입력하는 정수의 개수
nums = list(map(int, n[3].split())) # 입력하는 정수들

def find(arr, n):
    global pr
    global pl
    if pl > pr:
        print(0)
        return
    pc = (pr + pl) // 2
    if arr[pc] == n:
        print(1)
        return
    elif arr[pc] > i:
        pr = pc - 1
        find(arr, i)
    else:
        pl = pc + 1
        find(arr, i)
for i in nums:
    pr = N - 1
    pl = 0
    find(A, i)