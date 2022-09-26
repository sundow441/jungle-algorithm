import sys

sys.stdin = open('inputfile.txt','r')
n = int(sys.stdin.readline())
facto = n

if(n == 0):
    facto = 1
else:
    for i in range(n, 1, -1): # (start, stop, step)
        facto = facto * (i-1)
print(facto)