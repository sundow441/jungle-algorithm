import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()

testcase = int(n[0])
a = 0
float(a)
for i in range(1, testcase+1):
    m = list(map(float, n[i].split()))
    avg = float(format((sum(m) - m[0])/m[0]))
    for j in range(1, int(m[0]+1)):
        if(m[j] > avg):
            a = a + 1
    print("%.3f%%" % (a / m[0] * 100.000))
    a=0