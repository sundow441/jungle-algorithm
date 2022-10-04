from math import sqrt
from sys import stdin

stdin = open('inputfile.txt', 'r')
M, N, L = map(int, stdin.readline().split()) # 사대 수, 동물 수, 사정거리
m = list(map(int, stdin.readline().split())) # M개의 사대 좌표 리스트
n = []
for _ in range(N):
    n.append(list(map(int, stdin.readline().split()))) # N개의 동물 좌표 리스트
n, m = sorted(n), sorted(m)

count = 0
tmp = 0

for i in range(N):          
    pl = tmp
    pr = M - 1
    pc = 0
    while pr >= pl: 
        pc = (pl + pr) // 2
        if m[pc] <= n[i][0]: # 사대의 중간값이 동물 좌표의 x값보다 크지 않다면
            if M - 1 == pc or m[pc + 1] > n[i][0]: # ( +사대의 중간값이 최대값이거나, 중간값 오른쪽의 사대가 동물의 x좌표보다 크다면
                break # 탈출!
            pl = pc + 1 # 탐색 범위를 중간값 이상으로 한다
        else: # 사대의 중간값이 동물 좌표의 x값보다 크면
            pr = pc - 1 # 탐색 범위를 중간값 이하로 한다
    tmp = pc # 중간값을 tmp에 저장해 둔다
    if abs(n[i][0] - m[pc]) + n[i][1] <= L: # |(동물 좌표 x값) - 사대 중간값| + 동물 좌표 y값이 사정거리 이내라면
        count += 1 # 사냥 성공!
    elif M > pc + 1 and abs(n[i][0] - m[pc + 1])+ n[i][1] <= L: # 중간값이 사대 개수 이하이면서 사정거리 이내라면
        count += 1 # 사냥 성공!
print(count)

# 동물 좌표 기준 양쪽의 사대를 이분 탐색으로 찾아
# 사정거리 이내라면 count += 1