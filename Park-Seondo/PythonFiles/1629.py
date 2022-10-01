from sys import stdin

stdin = open('inputfile.txt', 'r')
n = stdin.read().splitlines()
A = int(n[0].split()[0])
B = int(n[0].split()[1])
C = int(n[0].split()[2])
ans = 1
for i in range(B):
    quotient = i

def gobsem(a, b):
    global ans
    while True:
        if b == 1:
            ans *= (a * b)
        elif b > 1:
            for i in b//2:



gobsem(A, B)
print(ans, C)
print(ans % C)