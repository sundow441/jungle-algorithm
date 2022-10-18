# from sys import stdin

# stdin = open("inputfile.txt", "r")
# N = int(stdin.readline())

# arr = [0 for _ in range(1000001)]
# arr[1] = 1
# arr[2] = 2
# for i in range(3, N + 1):
#     if arr[i] == 0:
#         arr[i] = (arr[i - 1] + arr[i - 2]) % 15746
# print(arr[N])

from sys import stdin
stdin = open("inputfile.txt", "r")

N = int(stdin.readline())
fibonacci = [0] * (10**6 + 1)

for i in range(N + 1):
    if i <= 3:
        fibonacci[i] = i % 15746
    else:
        fibonacci[i] = (fibonacci[i - 1] + fibonacci[i - 2]) % 15746

print(fibonacci[N])