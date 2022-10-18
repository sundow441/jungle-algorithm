from sys import stdin

stdin = open("inputfile.txt", "r")
N = int(stdin.readline())
nums = [list(map(int, stdin.readline().strip())) for _ in range(N)]
for i in nums:
    print(i)