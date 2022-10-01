import sys

sys.stdin = open('inputfile.txt','r')
m = sys.stdin.read().splitlines()
testcase = int(m[0])
n = []
for i in range(1, len(m)):
    n.append(int(m[i]))
