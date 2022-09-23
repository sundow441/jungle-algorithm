import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
for i in range(len(n)):
    nums = list(n[i])
print(nums)