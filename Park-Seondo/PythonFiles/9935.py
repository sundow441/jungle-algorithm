from collections import deque
from sys import stdin

stdin = open('inputfile.txt','r')
n = list(stdin.readline().strip())
m = list(stdin.readline())
stack = deque()

for i in range(len(n)):
    for j in range(len(m)):
        if len(stack) == 0 and n[i] == m[j]:
            stack.append(n[i])
        elif n[i - 1] in stack and n[i] == m[j]:
            stack.append(n[i])
for i in range(len(stack)):
    for j in m:
        if stack[i] == j:
            n.remove(j)
print("".join(n))