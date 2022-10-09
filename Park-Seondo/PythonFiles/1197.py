from sys import stdin

stdin = open('inputfile.txt','r')
V, E = list(map(int, stdin.readline().split())) #정점의 개수, 간선의 개수

root = [i for i in range(V + 1)] #루트를 저장하는 리스트(0 ~ V+1)

line = []
for i in range(E):
    line.append(list(map(int, stdin.readline().split()))) # 정점1, 2, 간선 저장

line.sort(key=lambda x:x[2]) #간선들을 가중치 순으로 정렬

def find(x): 
    if x != root[x]: #정점 x가 루트 리스트 안에 정렬되어 있지 않다면
        root[x] = find(root[x]) # 다시 검색
    return root[x] # root[x]를 반환(x)

ans = 0
for a, b, c in line: # 정점 a, b와 간선 c를 입력
    fromA = find(a) # 정점 a가 root일 때
    fromB = find(b) # 정점 b가 root일 때
    if fromA != fromB: # root 값이 서로 다르다면
        if fromA > fromB: # 큰 쪽을 작은쪽으로 변경
            root[fromA] = fromB
        else:
            root[fromB] = fromA
        ans += c # 간선 가중치를 더해줌

print(ans)