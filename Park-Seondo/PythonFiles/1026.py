from sys import stdin
stdin = open("inputfile.txt", "r")

N = int(stdin.readline())
A = sorted(list(map(int, stdin.readline().strip().split())))
B = sorted(list(map(int, stdin.readline().strip().split())), reverse=True)
ans = 0

for i in range(N):
    ans += (A[i] * B[i])
print(ans)