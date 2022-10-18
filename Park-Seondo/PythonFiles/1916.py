from heapq import heappop, heappush
from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

stdin = open("inputfile.txt", "r")
N = int(stdin.readline()) # 도시 개수
M = int(stdin.readline()) # 버스 개수

graph = [[] for _ in range(N + 1)]
gajungchi = [10**10 for _ in range(N + 1)] # 가중치 리스트를 최대로 초기화

for i in range(M):
    a, b, c = map(int, stdin.readline().strip().split())
    graph[a].append((b, c)) # 인접노드와 가중치를 함께 저장

target = list(map(int, stdin.readline().strip().split())) # 출발, 목표 지점

def Dijkstra(start):
    gajungchi[start] = 0 # 시작 노드의 가중치를 0으로 변경
    heap = []
    heappush(heap, [0, start]) # 초기 가중치와 출발지를 힙에 저장

    while heap:
        gajung, start1 = heappop(heap)
        if gajungchi[start1] < gajung: # 시작점의 가중치가 현재 가중치보다 작으면 컨티뉴
            continue
        for nextNode, nextNodeGajung in graph[start1]: # 그래프에서 인접노드와 가중치 꺼내오기
            totalGajung = gajung + nextNodeGajung # 가중치 총합 = 현재 노드 가중치 + 인접노드의 가중치
            if gajungchi[nextNode] > totalGajung: # 인접노드 번째 가중치가 현재 가중치 총합보다 크면
                gajungchi[nextNode] = totalGajung # 가중치 총합으로 변경
                heappush(heap, [totalGajung, nextNode]) # 힙에 가중치 총합과 인접 노드를 저장

Dijkstra(target[0])
print(gajungchi[target[1]])