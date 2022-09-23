import sys

sys.stdin = open('example.txt', 'r')

input = sys.stdin.read().split('\n')
print(input)

testcase = int(input[0])

print(5/3)
