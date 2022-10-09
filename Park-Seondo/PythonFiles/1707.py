from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open('inputfile.txt','r')
input = stdin.readline
K = int(input())

edge = []

def DFS(start, group): #DFS로 탐색
    global error

    if error: # error가 True일 때 재귀 빠져나오기
        return

    visited[start] = group # 그룹(1)에 넣기

    for i in graph[start]: # 인접한 노드를 탐색
        if not visited[i]: # 방문하지 않은 노드라면
            DFS(i, -group) # 인접한 노드이므로 다른 그룹(-1)에 저장
        elif visited[start] == visited[i]: # 인접한 노드와 서로 같은 그룹이라면
            error = True # error를 True로 바꾸고 반환
            return

for _ in range(K):
    V, E = map(int, input().split()) # 정점, 간선의 개수
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    error = False

    for _ in range(E):
        a, b = map(int, input().split()) # 인접한 노드 저장
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1): # 1번부터 마지막 노드까지 방문 여부 확인
        if not visited[i]:
            DFS(i, 1) # 방문하지 않은 노드라면 탐색
            if error:
                break

    if error:
        print("NO")
    else:
        print("YES")