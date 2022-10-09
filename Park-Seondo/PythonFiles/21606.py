from collections import deque
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open('inputfile.txt','r')
N =int(stdin.readline())
A = deque(map(int, stdin.readline().strip()))

graph = [[] for _ in range(N + 1)]

M = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = list(map(int, stdin.readline().strip().split()))
    graph[a].append(b)
    graph[b].append(a)


def a(graph, A):
    count = 0
    visited = [0 for _ in range(N + 1)]
    def DFS(start):
        cnt = 0
        for i in graph[start]: # 인접 노드 탐색
            if A[i - 1] == 1: # 해당 인접 노드가 실내라면
                cnt += 1 # 실내 카운트 +1
            else:
                if not visited[i]: # 인접 노드가 실외이며 방문하지 않았을 때
                    visited[i] = 1 # 해당 노드 방문
                    cnt += DFS(i) # 인접 노드와 인접한 실내를 다 돌 때 까지 재귀
        return cnt

    # DFS로 탐색을 못하는 실내 - 실내 인접의 경우
    for i in range(1, N + 1): # 1번부터 모든 노드를 다 돌면서
        if A[i - 1] == 1: # i번째 노드가 실내라면
            for j in graph[i]:
                if A[j - 1] == 1: # i의 인접 노드도 실내인지 확인
                    count += 1 # 카운트 + 1

        # 실내 - 실외의 경우
        else: # i번째 노드가 실외이며
            if not visited[i]: # 방문하지 않았다면
                visited[i] = 1 # 방문
                tmp = DFS(i) # 실외 노드와 인접한 실내 노드 모두 탐색
                count += tmp * (tmp - 1) # 인접 실내 * (실내 - 1) + 실내와 실내가 연결된 수
    return count

print(a(graph, A))