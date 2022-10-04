from heapq import heappop, heappush
from sys import stdin

stdin = open('inputfile.txt', 'r')
N = int(stdin.readline())
K = []
for _ in range(N):
    heappush(K, int(stdin.readline()))
tmp = 0
ans = 0
while len(K) > 1:
    tmp = (heappop(K) + heappop(K))
    ans += tmp
    heappush(K, tmp)
print(ans)