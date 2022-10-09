from sys import stdin, setrecursionlimit
setrecursionlimit(5000)

stdin = open('inputfile.txt','r')
N = int(stdin.readline()) # 정점의 개수
M = int(stdin.readline()) # 간선의 개수

graph = [[] for _ in range(N+1)]
for i in range(M): # 그래프의 정점 마다 연결되어있는 점 저장
    a, b = map(int, stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N + 1) # 방문지점 리스트

def DFS(start): # DFS를 사용 (시작 노드, 시작 노드의 깊이)
    visited[start] = 1 # 노드 방문 체크
    for i in graph[start]: # 시작점 기준으로 노드 하나씩 내려가면서 탐색
        if not visited[i]: # 방문하지 않은 노드일 경우 재귀
            DFS(i)

DFS(1) # 연결된 그래프가 있다면 DFS 탐색
print(sum(visited) - 1)