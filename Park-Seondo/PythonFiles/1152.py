import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
st = list(n[0].split())
print(len(st))