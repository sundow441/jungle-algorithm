import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
nums = list(map(int, n))

def solve(a):
    ans = 0
    for i in range(len(a)):
        ans = ans + a[i]
    print(ans)
    return ans

solve(nums)
#정수 n개가 주어졌을 때 n개의 합

# a: 합을 구해야 하는 정수 n개가 저장되어있는 배열
#(0 <= a[i] <= 1,000,000, 1 <= n <= 3,000,000)
# 리턴값 : a에 포함되어 있는 정수 n개의 합