from sys import stdin

stdin = open('inputfile.txt', 'r')
N = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
stack = []
point = []

for i in range(N):
    while True:
        if len(stack) <= 0:
            point.append(0)
            stack.append([i, towers[i]])
            break
        else:
            if stack[len(stack) - 1][1] < towers[i]:
                stack.pop()
            else:
                point.append(stack[len(stack) - 1][0] + 1)
                stack.append([i, towers[i]])
                break
print(*point)

# 앞에서부터 순차적으로 탐색
# 스택이 비었으면 point에 0을 추가하고 stack에 인덱스와 높이를 추가
# 스택이 비지 않았으면 현재 stack에 있는 높이들에 대해 탐색
# 현재 탑의 높이보다 낮은 것들은 pop 하고, 높다면 해당 탑의 index를 point에 추가, stack에 현재 탑 추가

# for i in range(N - 1, -1, -1):
#     for j in range(i - 1, -1, -1):
#         if towers[i] <= towers[j]:
#             point.insert(0, j + 1)
#             break
#         elif j == 0 and towers[i] > towers[0]:
#             point.insert(0, 0)
# point.insert(0, 0)
# print(*point)