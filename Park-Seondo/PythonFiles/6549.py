from collections import deque
from sys import stdin

stdin = open('inputfile.txt', 'r')

while True:
    h = list(map(int, stdin.readline().split()))
    n = h.pop(0)

    if n == 0:
        break
    
    stack = deque()
    ans = 0

    for i in range(n):
        while len(stack) != 0 and h[stack[-1]] > h[i]:
            tmp = stack.pop()
            
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] -1
            ans = max(ans, width * h[tmp])
        stack.append(i)

    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] -1
        ans = max(ans, width * h[tmp])
    print(ans)