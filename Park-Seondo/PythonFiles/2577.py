import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
nums = list(map(int, n))
a = nums[0]
for i in range(1, len(nums)):
    a = a * nums[i]

st = list(str(a))
st = list(map(int, st))
count = [0 for l in range(10)]

for j in range(len(st)):
    for k in range(10):
        if(count[k] == 0 and st[j] != k):
            count[k] = 0
        elif(st[j] == k):
            count[k] = count[k] + 1

for m in range(len(count)):
    print(count[m])
