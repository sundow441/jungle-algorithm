import sys

sys.stdin = open('inputfile.txt', 'r')
n = sys.stdin.read().splitlines()
N, r, c = map(int, n[0].split())

result = 0

while N != 0:
    N -= 1
    if r < 2 ** N and c < 2 ** N:
        result += (2 ** N) * (2 ** N) * 0
    elif r < 2 ** N and c >= 2 ** N:
        result += (2 ** N) * (2 ** N) * 1
        c -= (2 ** N)
    elif r >= 2 ** N and c < 2 ** N:
        result += (2 ** N) * (2 ** N) * 2
        r -= (2 ** N)
    else:
        result += (2 ** N) * (2 ** N) * 3
        r -= (2 ** N)
        c -= (2 ** N)
print(result)