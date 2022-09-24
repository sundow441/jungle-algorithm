import sys

sys.stdin = open('inputfile.txt','r')
nums = list(map(int, sys.stdin.readline().split()))
N = 0
days = nums[2] - nums[0] + 1
print(days)