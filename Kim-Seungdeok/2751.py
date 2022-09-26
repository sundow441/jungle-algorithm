import sys

sys.stdin = open('example.txt', 'r')

input = list(map(int,sys.stdin.read().strip().split()))

testCase = input[0]

input.pop(0)

nums = input

for i in range(testCase):
    maxNum = max(nums)
    nums.remove(maxNum)
    print(maxNum)
