import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
testcase = int(n[0])
n.remove(n[0])
n = list(map(int, n))

def shellSort(a):

    h = 1

    while(h < len(a) // 9):
        h = h * 3 + 1

    while(h > 0):
        for i in range(h, len(a)):
            j = i - h
            temp = a[i]
            while(j >= 0 and a[j] > temp):
                a[j + h] = a[j]
                j -= h
            a[j + h] = temp
        h //= 3
shellSort(n)
for j in range(len(n)):
    print(n[j])