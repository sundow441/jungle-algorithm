import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()

for i in range(1, len(n)):
    m = list(map(int, n[i].split()))
    print(m[0]+m[1])