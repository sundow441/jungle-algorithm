from sys import stdin
stdin = open("inputfile.txt", "r")
N, K = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))

tab = [0] * N # 멀티탭 구멍 개수만큼 0으로 초기화한 리스트 생성
count = 0 # 플러그를 뽑는 횟수
idx = 0
tmp = 0
tmp_idx = 0
for i in arr:
    if i in tab: #멀티탭에 동일한 제품이 있을 경우
        pass
    elif 0 in tab: # 멀티탭에 빈 칸이 있을 경우
        tab[tab.index(0)] = i # 현재 제품번호로 변경
    else: # 멀티탭에 빈자리도 없고 동일한 제품이 없을 경우
        for j in tab:
            # 남은 제품 리스트에 현재 멀티탭에 있는 제품이 없다면
            if j not in arr[idx:]:
                tmp = j # 뽑을 제품 tmp에 저장
                break
            #남은 제품 리스트에 현재 멀티탭에 있는 제품이 있다면
            elif arr[idx:].index(j) > tmp_idx: # 더 나중에 있는 것을 뽑는다
                tmp = j
                tmp_idx = arr[idx:].index(j)
        tab[tab.index(tmp)] = i # 뽑은 제품의 자리에 현재 제품사용
        tmp = tmp_idx = 0
        count += 1
    idx += 1
print(count)