from sys import stdin
from collections import deque

stdin = open('inputfile.txt', 'r')
N, K = map(int, stdin.readline().split())
nums = deque()
for i in range(N):
    nums.append(i + 1)

j = K - 1
ans = []
for _ in range(N):
    for j in range(K - 1):
        nums.append(nums.popleft())
    ans.append(nums.popleft())
    j += K - 1
    if j >= len(nums):
        j -= len(nums)
print("<", end="")
for i in range(len(ans) - 1):
    print(ans[i], end=", ")
print(ans[-1], end="")
print(">")