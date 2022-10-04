from sys import stdin

stdin = open('inputfile.txt', 'r')
T = int(stdin.readline())

for i in range(T):
    stack = []
    A = stdin.readline()
    for j in A:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break     
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")