from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open('inputfile.txt','r')
N = int(stdin.readline())

Graph = [[] for _ in range(N + 1)]

Parents = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, stdin.readline().strip().split())
    Graph[a].append(b)
    Graph[b].append(a)

def DFS(start, graph, parents):
    for i in graph[start]: # 루트로부터 인접한 노드를 탐색
        if parents[i] == 0: # 인접한 노드의 부모가 저장되어 있지 않다면
            parents[i] = start # 자신을 부모로 저장
            DFS(i, graph, parents) #재귀
DFS(1, Graph, Parents)

for i in range(2, N + 1): # 루트 노드를 제외한 모든 노드의 부모를 출력
    print(Parents[i])