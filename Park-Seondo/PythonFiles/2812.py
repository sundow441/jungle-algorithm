from sys import stdin

stdin = open('inputfile.txt', 'r')
N, K = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().strip()))
stack = []

count = N

for i in range(N):
    while True:
        if len(stack) == 0 or count <= (N - K) - len(stack):
            stack.append(nums[i])
            break
        else:
            if stack[len(stack) - 1] < nums[i]:
                stack.pop()
            elif (N - K) - len(stack) >= 1 and stack[len(stack) - 1] >= nums[i]:
                stack.append(nums[i])
                break
            else:
                break
    count -= 1

stack = list(map(str, stack))
stack = int("".join(stack))
print(stack)