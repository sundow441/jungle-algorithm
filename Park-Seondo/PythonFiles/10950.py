import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
testcase = int(n[0])
for i in range(1, testcase+1):
    m = list(map(int, n[i].split()))
    print(m[0]+m[1])