import sys

sys.stdin = open('inputfile.txt','r')
nums = list(map(int, sys.stdin.readline().strip().split()))

days = (nums[2] - nums[1]) / (nums[0] - nums[1])
if(days > int(days)):
    days = days+1

print(int(days)) 