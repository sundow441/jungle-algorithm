import sys

sys.stdin = open('inputfile.txt', 'r')
n = int(sys.stdin.readline())
result = 0
row = [0] * n

def isPromising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def nQueen(x):
    global result
    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if isPromising(x):
                nQueen(x + 1)
nQueen(0)
print(result)