from sys import stdin
stdin = open("inputfile.txt", "r")
string_A = list(stdin.readline().strip())
string_B = list(stdin.readline().strip())
LCS = [[0] * (len(string_A) + 1) for _ in range(len(string_B) + 1)]
ans = 0
for i in range(len(string_B) + 1):
    for j in range(len(string_A) + 1):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif string_B[i - 1] == string_A[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
for i in LCS:
    print(i)
for i in LCS:
    if ans < max(i):
        ans = max(i)
print(ans)