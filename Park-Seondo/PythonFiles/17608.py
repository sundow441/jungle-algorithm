from sys import stdin

stdin = open('inputfile.txt', 'r')
N = int(stdin.readline())
stack = []
cnt = 1

for j in range(N):
    stack.append(int(stdin.readline()))

lastStack = stack[N - 1]

for i in range(N -1, -1, -1):
    if stack[i] > lastStack:
        cnt += 1
        lastStack = stack[i]
print(cnt)