from heapq import heappop, heappush
from sys import stdin

stdin = open('inputfile.txt', 'r')
N = int(stdin.readline())

smallarr = [] # 기준치 보다 작은 값을 담을 리스트
bigarr = [] # 기준치 보다 큰 값을 담을 리스트
ans = []    # 가운데 값을 담을 리스트
for i in range(N):
    num = int(stdin.readline())
    if len(smallarr) == len(bigarr): # 양쪽의 원소 개수가 같다면
        heappush(smallarr, (-num, num)) # 작은 쪽에 원소 거꾸로 추가
    else:
        heappush(bigarr, (num, num))    # 아니라면 큰 쪽에 원소 추가(양쪽 개수 균형 맞추기 위함)
    if bigarr and smallarr[0][1] > bigarr[0][0]: # 작은 쪽의 최대값이 큰 쪽의 최소값 보다 크다면
        min = heappop(bigarr)[0]    # 원소를 서로 교환
        max = heappop(smallarr)[1]
        heappush(smallarr, (-min, min))
        heappush(bigarr, (max, max))
    ans.append(smallarr[0][1])  # ans에 가운데 값들만 모음

for i in ans:   # 출력
    print(i)

# 총 개수가 홀수라면 정확히 가운데 값이 작은 배열로 들어가고,
# 짝수라도 가운데 두 값 중 작은쪽이 작은 배열로 들어가므로
# 작은쪽 배열의 루트(가장 큰 값)를 출력 해주면 된다