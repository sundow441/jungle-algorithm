from sys import stdin

stdin = open('inputfile.txt','r')
n = list(map(int, stdin.read().strip().split()))

def postorder(lc, rc):
    if lc > rc:
        return

    endPoint = rc + 1

    for i in range(lc + 1, rc + 1):
        if n[lc] < n[i]:
            endPoint = i
            break
    postorder(lc + 1, endPoint - 1)
    postorder(endPoint, rc)

    print(n[lc])

postorder(0, len(n)-1)