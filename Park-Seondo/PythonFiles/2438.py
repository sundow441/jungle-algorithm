import sys

sys.stdin = open('inputfile.txt','r')
num = int(sys.stdin.read())

for i in range(num):
    for j in range(i+1):
        if(j == i):
            print("*")
        else:
            print("*", end='')