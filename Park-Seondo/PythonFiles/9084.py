from sys import stdin
stdin = open("inputfile.txt", "r")

T = int(stdin.readline()) # 테스트 케이스
for i in range(T):
    N = int(stdin.readline()) # 동전 종류
    coins = list(map(int, stdin.readline().strip().split())) # 동전 리스트
    coins.insert(0, 0) # 0을 추가
    target = int(stdin.readline()) # 만들어야 하는 금액

    graph = [[0] * (target + 1) for i in range(N + 1)] # 동전 종류 + 1과 만들 금액 + 1 만큼 2차원 행렬 생성
    for i in range(N + 1): #만들 금액이 0인 경우 0개로 밖에 만들어지지 않으므로 1로 초기화
        graph[i][0] = 1

    for j in range(1, N + 1):
        for i in range(1, target + 1):
            graph[j][i] = graph[j - 1][i] # 이전 동전으로 만들수 있는 경우로 초기화(여기에 현재 동전으로 만들 수 있는 경우를 추가)
            if i - coins[j] >= 0: # 타겟 금액 - 현재 동전이 0보다 작지 않다면
                graph[j][i] += graph[j][i - coins[j]] # 현재 동전으로 만들 수 있는 경우 += (현재 타겟 - 현재 동전)번째 경우
    print(graph[N][target])