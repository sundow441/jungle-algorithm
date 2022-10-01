from sys import stdin

stdin = open('inputfile.txt', 'r')
n = stdin.read().splitlines()
N, K = int(n[0].split()[0]), int(n[0].split()[1])
n.remove(n[0])
X = sorted(list(map(int, n)))

pl = min(X)
pr = pl + K

ans = 0

while pl <= pr: # 현재 최소 레벨이 +K보다 작거나 같을 때
    pc = (pl + pr) // 2 # 중간 값

    hap = 0
    for i in X: # 현재 레벨 리스트에서 하나씩 꺼냄
        if pc > i: # 현재 레벨이 중간 값보다 작을 때
            hap += (pc - i) # 중간값과 현재 레벨의 차 만큼 변수에 저장한다
    if hap <= K: # 올려야 하는 레벨이 올릴 수 있는 레벨보다 작으면
        pl = pc + 1 # 최소 레벨을 중간값 +1로 변경
        ans = max(pc, ans) # 중간값과 저장된 값 중 큰 값을 저장
    else:
        pr = pc - 1 #나머지의 경우 최대 레벨을 중간값 - 1로 내임
print(ans)
