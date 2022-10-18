from sys import stdin
stdin = open("inputfile.txt", "r")

INF = 2**31
N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

DP = [[0] * N for _ in range(N)]

for dia in range(1, N): # DP[dia][dia]는 자기 자신이기 때문에 0
    for i in range(0, N - dia): # 중앙 대각선으로부터 한 칸씩 옮김
        j = i + dia # 연재 행의 중앙 대각선으로부터 몇번째 원소인지
        if dia == 1: # 서로 차이가 1밖에 나지 않는 칸은 그냥 서로 곱함
            DP[i][j] = arr[i][0] * arr[j][0] * arr[j][1]
            continue
        DP[i][j] = float(INF) # 나머지 원소는 최대값으로 초기화
        for k in range(i, j):
            DP[i][j] = min(DP[i][j], DP[i][k] + DP[k + 1][j] + arr[i][0]
            * arr[k][1] * arr[j][1])
print(DP[0][N - 1])