from sys import stdin
stdin = open("inputfile.txt", "r")

T = int(stdin.readline())
n = [int(stdin.readline().strip()) for _ in range(T)]

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return solution(n - 1) + solution(n - 2) + solution(n - 3)

for i in n:
    print(solution(i))