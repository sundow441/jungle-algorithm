from sys import stdin

stdin = open('inputfile.txt', 'r')
n = stdin.read().splitlines()
N, M= int(n[0].split()[0]), int(n[0].split()[1]) # 나무의 수, 가져갈 나무의 길이
Trees = list(map(int, n[1].split())) # 나무의 높이 리스트
pr = max(Trees)
pl = 0
pc = (pr + pl) // 2
a = 0
def cutTree(arr, l):
    global pr
    global pl
    global pc
    global a
    while pr >= pl:
        logs = 0 #자른 통나무 길이 리스트

        for i in arr:
            if i - pc > 0:
                logs += (i - pc)
                
        if logs > l:
            a = pc
            pl = pc + 1
            pc = (pr + pl) // 2
        elif logs == l:
            print(pc)
            return
        else:
            a = pc
            pr = pc - 1
            pc = (pr + pl) // 2
    if pr < pl:
        print(pc)
    
cutTree(Trees, M)