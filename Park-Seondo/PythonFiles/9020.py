import sys
import math

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
testcase = int(n[0])
n.remove(n[0])
n = list(map(int, n))
x = []
primeNumArr = []
smallNum = 10000
bigNum = 0
a = 10000

for i in range(1, 100):
    if(i == 2 or i == 3 or i == 5 or i == 7):
        x.append(i)
        primeNumArr.append(i)
    elif(i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i != 1):
        x.append(i)
        primeNumArr.append(i)

