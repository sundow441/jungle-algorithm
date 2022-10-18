# from sys import stdin

# stdin = open("inputfile.txt", "r")
# n = int(stdin.readline())

# arr = [0 for i in range(n + 1)]

# def fibonachi():
#     for i in range(n + 1):
#         if arr[i] == 0:
#             if i == 1 or i == 2:
#                 arr[i] = 1
#             elif i > 2:
#                 arr[i] = arr[i - 1] + arr[i - 2]
#     return arr[-1]
# print(fibonachi())

from sys import stdin
stdin = open("inputfile.txt", "r")

n = int(stdin.readline())
nums = [0] * (n + 1)

def fibo(num, arr):
    if num == 1 or num == 2:
        return 1
    if arr[num] != 0:
        return arr[num]
    arr[num] = fibo(num - 1, arr) + fibo(num - 2, arr)
    return arr[num]

print(fibo(n, nums))