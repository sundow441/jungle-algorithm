from sys import stdin
stdin = open("inputfile.txt", "r")

N = int(stdin.readline())
A = list(map(int, stdin.readline().strip().split()))

DP = [1] * N

for i in range(1, N):
    for j in range(i): # i와 i - 1까지의 수를 비교
        if A[i] > A[j]: # i가 더 크면
            DP[i] = max(DP[i], DP[j] + 1) # DP[i]의 값과 DP[j]에 1을 더한 값을 비교해 더 큰 값을 DP[i]에 저장
print(max(DP)) # DP의 값 중 가장 큰 값을 출력