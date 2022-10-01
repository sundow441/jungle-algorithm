import sys

sys.stdin = open('inputfile.txt', 'r')
n = sys.stdin.read().splitlines()
N = int((n[0].split()[0]))
M = int((n[0].split()[1]))
n.remove(n[0])
n = list(map(int, n[0].split()))
maxBJ = 0

def blackJack(arr, r):
    cardlist = []
    if r > len(arr):
        return cardlist
    
    if r == 1:
        for i in arr:
            cardlist.append([i])
    
    elif r > 1:
        for i in range(N - r + 1):
            for j in blackJack(arr[i + 1:], r - 1):
                cardlist.append([arr[i]] + j)
    return cardlist

for i in blackJack(n, 2):
    print(i)
    if sum(i) <= M:
        if maxBJ < sum(i):
            maxBJ = sum(i)
print(maxBJ)