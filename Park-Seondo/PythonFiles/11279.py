from heapq import heappop, heappush
from sys import stdin

stdin = open('inputfile.txt', 'r')
N = int(stdin.readline()) # 연산 개수
x = list(map(int, stdin.read().strip().split()))

arr = []
for i in x:
    if i == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heappop(arr))
    else:
        heappush(arr, -i)

# def heapsort(arr, left, right):
#     tmp = arr[left]
#     parent = left
#     while parent < (right + 1) // 2:

#         cl = parent * 2 + 1
#         cr = cl + 1

#         if cr <= right and arr[cr] > arr[cl]:
#             child = cr
#         else:
#             child = cl
#         if tmp >= arr[child]:
#             break
#         arr[parent] = arr[child]
#         parent = child
#     arr[parent] = tmp

# arr = deque()
# for i in x:
#     if i == 0:
#         if len(arr) == 0:
#             print(0)
#         else:
#             for j in range((len(arr) - 1)//2, -1, -1):
#                 heapsort(arr, j, len(arr) - 1)
#             print(arr[0])
#             arr.popleft()
#     else:
#         arr.append(i)