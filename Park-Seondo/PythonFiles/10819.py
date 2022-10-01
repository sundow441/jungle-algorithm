import sys

sys.stdin = open('inputfile.txt', 'r')
n = sys.stdin.read().splitlines()
N = int(n[0])
n.remove(n[0])
A = list(map(int, n[0].split()))
A.sort()    #값 정렬
 
def next_permutation(list_a):
    k = -1
    m = -1
 
    # 증가하는 마지막 부분을 가리키는 index k 찾기
    for i in range(len(list_a)-1):
        if list_a[i] < list_a[i+1]:
            k = i
 
    # 전체 내림차순일 경우, 반환
    if k == -1:
        return [-1]
 
    # index k 이후 부분 중 값이 k보다 크면서 가장 멀리 있는 index m 찾기
    for i in range(k, len(list_a)):
        if list_a[k] < list_a[i]:
            m = i
 
    # k와 m의 값 바꾸기
    list_a[k], list_a[m] = list_a[m], list_a[k]
 
    # k index 이후 오름차순 정렬
    list_a = list_a[:k+1] + sorted(list_a[k+1:])
    return list_a
 
ans = 0
# 첫 순열 내 값 차이를 더해(s), ans 보다 크면 ans를 update
s = 0
for j in range(len(A) - 1):
    s += abs(A[j] - A[j+1])
if s > ans:
    ans = s
 
arr = A
 
while True:
    arr = next_permutation(arr)
    if arr == [-1]:
        break
    s = 0
 
    # 순열마다 차이를 더해(s), ans 보다 크면 ans를 update
    for j in range(len(arr) - 1):
        s += abs(arr[j] - arr[j+1])
    if s > ans:
        ans = s
 
print(ans)



# def permu(arr, r):
#     numlist = []

#     if r == 1:
#         for i in arr:
#             numlist.append([i])
#     elif r > 1:
#         for i in range(N):
#             for j in permu(arr, r - 1):
#                 if len([arr[i]] + j) == len(set([arr[i]] + j)):
#                     numlist.append([arr[i]] + j)
#     return numlist

# NSum = 0
# NSum2 = []
# for i in permu(A, N):
#     for j in range(N - 1):
#         NSum2.append(abs(i[j] - i[j+1]))
#     if NSum < sum(NSum2):
#         NSum = sum(NSum2)
#     NSum2 = []
# print(NSum)