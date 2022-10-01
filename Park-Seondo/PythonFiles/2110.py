from sys import stdin

stdin = open('inputfile.txt', 'r')
n = stdin.read().splitlines()
N, C= int(n[0].split()[0]), int(n[0].split()[1])
n.remove(n[0])
n = sorted(list(map(int, n)))

for i in range(len(n) - 1):
    if i < len(n) - 1:
        a = n[i + 1] - n[i]

def build(arr, pl, pr):
    ans = 0
    while pl <= pr:
        pc = (pr + pl)  // 2
        distance = arr[0]
        count = 1
        
        for i in range(1, len(arr)):
            if arr[i] >= distance + pc:
                count += 1
                distance = arr[i]

        if count >= C:
            pl = pc + 1
            ans = pc
        else:
            pr = pc - 1
    
    print(ans)
build(n, 1, n[len(n) - 1] - n[0])