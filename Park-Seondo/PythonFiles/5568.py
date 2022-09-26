from random import Random
import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()

num = []
for i in range(len(n)):
    num.append(int(n[i]))
testcase = num[1]
n.remove(n[0])
k = int(n[0])
n.remove(n[0])
    
