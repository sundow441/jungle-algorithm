from sys import stdin
from collections import deque

stdin = open('inputfile.txt', 'r')
N = int(stdin.readline())
queue = deque()
for i in range(N):
    queue.append(i + 1)

tmp = 0
count = 1
while len(queue) > 1:
    if count % 2 == 0:
        tmp = queue[0]
        queue.popleft()
        queue.append(tmp)
    else:
        queue.popleft()
    count += 1
print(*queue)