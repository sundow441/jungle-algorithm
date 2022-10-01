from sys import stdin

stdin = open('inputfile.txt', 'r')
n = stdin.read().splitlines()
N = int(n[0].split()[0])
n.remove(n[0])
papers = []
for i in n:
    papers.append(list(map(int, i.split())))
    
blueBox = 0
whiteBox = 0
def cutPaper(n, paper):
    global whiteBox
    global blueBox
    temp = []
    check = 0

    for i in range(n):
        check += sum(paper[i])
    if check == n * n:
        blueBox += 1
    elif check == 0:
        whiteBox += 1
    else:
        for i in range(0,n//2): # 1사분면 0 ~ 3, 0 ~ 1, 0
            temp.append([*paper[i]][0:n//2])
        cutPaper(n//2, temp)
        temp = []

        for i in range(0,n//2): # 2사분면 0 ~ 3, 0 ~ 1, 1
            temp.append([*paper[i]][n//2:n])
        cutPaper(n//2, temp)
        temp = []

        for i in range(n//2,n): # 3사분면 4 ~ 7, 2 ~ 3, 2
            temp.append([*paper[i]][0:n//2])
        cutPaper(n//2, temp)
        temp = []

        for i in range(n//2,n): # 4사분면 4 ~ 7, 2 ~ 3, 3
            temp.append([*paper[i]][n//2:n])
        cutPaper(n//2, temp)
        temp = []
cutPaper(N, papers)
print(whiteBox)
print(blueBox)