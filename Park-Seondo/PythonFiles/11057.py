from sys import stdin
stdin = open("inputfile.txt", "r")

N = int(stdin.readline())
graph = [[0] * 10 for _ in range(N)]

ans = 0  
def a(ans):
    for i in range(10):
        graph[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            graph[i][j] = sum(graph[i - 1][j:])
            if graph[i][j] < 0:
                graph[i][j] = 0
    ans += sum(graph[-1])
    print(ans % 10007)
a(ans)