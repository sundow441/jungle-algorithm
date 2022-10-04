from sys import stdin

stdin = open('inputfile.txt', 'r')
k = int(stdin.readline())
stack = []

for i in range(k):
    n = int(stdin.readline())
    if n != 0:
        stack.append(n)
    elif n == 0:
        stack.pop()
print(sum(stack))