import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
n = int(n[0])
count = 0
num = []

for i in range(1, n + 1):
    if(i < 100):
        count += 1
    elif(i >= 100):
        num = list(str(i))
        num = list(map(int, num))
        if(num[2] - num[1] == num[1] - num[0]):
            count += 1
print(count)
