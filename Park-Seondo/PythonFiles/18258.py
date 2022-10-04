from sys import stdin

stdin = open('inputfile.txt', 'r')
N = int(stdin.readline())
queue = []
head = 0

for i in range(N):
    tail = len(queue)
    order = stdin.readline().split()
    if order[0] == "push":
        queue.append(order[1])
    elif order[0] == "pop":
        if head >= len(queue):
            print(-1)
        else:
            print(queue[head])
            head += 1
    elif order[0] == "size":
        print(tail - head)
    elif order[0] == "empty":
        if head >= len(queue):
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if head >= len(queue):
            print(-1)
        else:
            print(queue[head])
    elif order[0] == "back":
        if head >= len(queue):
            print(-1)
        else:
            print(queue[tail - 1])