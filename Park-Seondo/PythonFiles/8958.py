import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
testcase = int(n[0])
score = 0
a = 0
for i in range(1, testcase + 1):
    m = list(n[i])
    for j in range(len(m)):
        if(m[j]=='O'):
            a = a + 1
            score = score + a
        elif(m[j]=='X'):
            a = 0
    a = 0
    print(score)
    score = 0