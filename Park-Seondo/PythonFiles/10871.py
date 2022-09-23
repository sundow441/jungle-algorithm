import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()

testcase = list(map(int, n[0].split()))
nums = list(map(int, n[1].split()))

for i in range(testcase[0]):
    if(nums[i] < testcase[1]):
        print(nums[i],"", end='')