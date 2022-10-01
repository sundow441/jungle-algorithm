import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
testcase = int(n[0])
n.remove(n[0])

nums = []
for i in range(len(n)):
    nums.append(int(n[i]))

def bubbleSort(a):
    for o in range(len(a)):
        for j in range(len(a) - 1, 0, -1):
            if(a[j] < a[j - 1]):
                a[j], a[j -1] = a[j -1], a[j]
        print(a[o])
bubbleSort(nums)