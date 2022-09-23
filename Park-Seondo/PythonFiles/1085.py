import sys

sys.stdin = open('inputfile.txt','r')
x, y, w, h = map(int, input().split())

a = w - x
b = h - y

if(a < b and a < x and a < y):
    print(a)
elif(b < a and b < x and b < y):
    print(b)
elif(x < a and x < b and x < y):
    print(x)
else:
    print(y)