import heapq
import sys
from sys import stdin

stdin = open('inputfile.txt', 'r')
n = int(stdin.readline())
road_info = []
for _ in range(n):
    road = list(map(int, stdin.readline().split()))
    road_info.append(road)

d = int(stdin.readline())
roads = []
for road in road_info:
    house, office = road
    if abs(house - office) <= d:
        road = sorted(road)
        roads.append(road)
roads.sort(key=lambda x:x[1])

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)


# arr = deque()
# maxValue = 0
# for i in range(N):
#     for j in range(N):
#         if n[j][1] <= n[i][1] and n[j][0] >= (n[i][1] - d):
#             if abs(n[j][1] - n[j][0]) <= d:
#                 arr.append(n[j][0])
#                 if maxValue < len(arr):
#                     maxValue = len(arr)
#             if len(arr) > 0 and n[j][1] - arr[0] > d:
#                 arr.popleft()
#     arr.clear()
# print(maxValue)