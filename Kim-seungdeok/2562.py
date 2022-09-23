import sys

sys.stdin = open('example.txt', 'r')

input = sys.stdin.read().split('\n')

input = list(map(int, input))

print(input)

print(max(input))
print(input.index(max(input))+1)