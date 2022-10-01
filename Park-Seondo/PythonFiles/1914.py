import sys

sys.stdin = open('inputfile.txt', 'r')
n = int(sys.stdin.readline())

def HanoiTower(first, second, third, count):
    if count >=1:
        HanoiTower(first, third, second, count - 1)
        print(first, third)
        HanoiTower(second, first, third, count - 1)

print(2 ** n - 1)

if n <= 20:
    HanoiTower(1, 2, 3, n)