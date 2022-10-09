import sys
from bisect import bisect_left
input = sys.stdin.readline
sys.setrecursionlimit(400000)

def next_circle(cur_c,next_c):
    global cnt
    if circles[cur_c][1] == circles[next_c][1]:
        cnt += 1
        return
    tmp = bisect_left(circles,(circles[next_c][1],))
    if tmp == len(circles):
        return
    if circles[tmp][0]==circles[next_c][1]:
        next_circle(cur_c,tmp)


n = int(input())
circles = []
for i in range(n):
	x,r = map(int,input().split())
	circles.append((x-r,x+r))
circles.sort(key=lambda x:(x[0],-x[1]))

cnt = 0
for i in range(n-1):
	if circles[i][0] == circles[i+1][0]:
		next_circle(i,i+1)
print(n+cnt+1)