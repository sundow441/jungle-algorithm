import sys

sys.stdin = open('inputfile.txt', 'r')
n = sys.stdin.read().splitlines()
nanjengi = list(map(int, n))
realNanjeng = []

def nanjeng(arr, r):
    nanjenglist = []
    if r > len(arr):
        return nanjenglist

    if r == 1:
        for i in arr:
            nanjenglist.append([i])

    elif r > 1:
        for i in range(len(arr) - r + 1):
            for j in nanjeng(arr[i + 1:], r - 1):
                nanjenglist.append([arr[i]] + j)
    return nanjenglist

for i in nanjeng(nanjengi, 7):
    if sum(i) == 100:
        realNanjeng = i
for i in range(7):
    print(sorted(realNanjeng)[i])