from sys import stdin

stdin = open("inputfile.txt", "r")
N = int(stdin.readline().strip())
graph = [[] for _ in range(N + 1)]
a = []
for i in range(N):
    a.append(list(map(int, stdin.readline().strip().split())))

for i in range(1, N + 1):
    if i == 1:
        graph[i] = a[i - 1][0]
    elif i <= N:
        graph[i] = ((a[i - 1][0], a[i - 1][1]))
print(graph)