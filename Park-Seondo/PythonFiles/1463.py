from sys import stdin
stdin = open("inputfile.txt", "r")

N = int(stdin.readline())
count = 0
while N != 1:
    if (N - 1) % 3 == 0:
        count += 2
        N //= 3
    elif N % 3 != 0:
        if N % 2 != 0:
            N -= 1
            count += 1
        elif N % 2 == 0:
            count += 1
            N //= 2
    elif N % 3 == 0:
        count += 1
        N //= 3
print(count)