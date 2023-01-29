from sys import stdin
stdin = open("inputfile.txt", "r")

def solution(N, W, dp):
    for i in range(N):
        for j in range(N):
            if not W[i][j]:
                W[i][j] = float('inf')
    for i in range(1, N):
        dp[i][0] = W[i][0]

    for k in range(1, N - 1):
        for route in range(1, size):
            if count(route, N) == k:
                for i in range(1, N):
                    if not isin(i, route):
                        dp[i][route] = getMinimum(N, W, i, route, dp)
    dp[0][size - 1] = getMinimum(N, W, 0, size - 1, dp)

    return dp[0][size - 1]

def count(route, N):
    cnt = 0
    for n in range(1, N):
        if route & (1 << n - 1) != 0:
            cnt += 1
    return cnt

def isin(i, route):
    if route & (1 << i - 1) != 0:
        return True
    else:
        return False

def getMinimum(N, W, i, route, dp):
    minimumDist = float('inf')
    for j in range(1, N):
        if isin(j, route):
            beforeRoute = route & ~(1 << j - 1)
            dist = W[i][j] + dp[j][beforeRoute]
            if minimumDist > dist:
                minimumDist = dist
    return minimumDist

N = int(stdin.readline())
W = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]
size = 2 ** (N - 1) # 비트마스킹 하기 위한 크기 설정
DP = [[float('inf')] * size for _ in range(N)] # 최소값을 구해야 하기 때문에 inf로 초기화

print(solution(N, W, DP))