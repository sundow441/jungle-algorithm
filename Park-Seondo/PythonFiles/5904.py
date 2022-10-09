from collections import deque
from sys import stdin

stdin = open('inputfile.txt','r')
# n = int(stdin.readline())

# arr = ["m", "o"]
# ans = deque()
# k = []
# for i in range(n):
#     k.append(int(i) + 1)
# for i in range(n):
#     ans.append(arr[0])
#     ans.append(arr[1])
#     ans.append(arr[1])
#     if i >= 1:
#         ans.append(arr[0])
#         for _ in range(i + 2):
#             ans.append(arr[1])
# def moo(k):
#     global ans
#     if k == 1:
#         ans.append(arr[0])
#         for _ in range(k + 1):
#             ans.append(arr[1])
#         return ans
#     else:
#         ans = moo(k - 1)
#         ans.append(moo(1))
#         ans.append(arr[0])
#         for _ in range(k + 1):
#             ans.append(arr[1])
#         return ans
# print(moo(n)[n])

N = int(stdin.readline())

def moo(acc, cur, N): #Moon(n)의 길이, 가운데 부분의 길이, N
    prev = (acc-cur)//2 # Moon(n - 1)은 총 길이(Moon(n))에서 가운데 길이를 빼고 2로 나눈 것과 같음
    if N <= prev: return moo(prev, cur-1, N) # 가운데에 N이 존재한다면 한개의 m과 (n+2)개의 o로 구성되어 있기 때문에
    elif N > prev+cur: return moo(prev, cur-1, N-prev-cur)
    else: return "o" if N-prev-1 else "m" # N 이 가운데의 첫번째라면 m, 아니라면 o

acc, n = 3, 0
while N > acc: # Moo(n)의 길이가 N이상이어야 하기 때문에 이를 만족하는 n을 찾음
    n += 1 
    acc = acc*2+n+3 # Moo(n - 1) * 2 + (n + 3) 3은 기본 "Moo"

print(moo(acc, n+3, N))

# Moo(n) = Moo(n-1) + "m" + "o"*(n+2) + Moo(n-1)
# 양쪽의 Moo(n-1) 부분과 가운데 "m" + "o"*(n+2) 부분으로 나눌 수 있음.
# N번째 문자는 왼쪽, 오른쪽 Moo(n-1)과 가운데"m" + "o"*(n+2)중 한군데에 존재
# Moo(n)의 길이가 N이상이어야 하기 때문에 이를 만족하는 n을 찾음
# Moo(n - 1) * 2 + (n + 3) 3은 기본 "Moo"
# 