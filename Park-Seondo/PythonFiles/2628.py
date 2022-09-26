import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()

extent = list(map(int, n[0].split()))
n.remove(n[0])
testcase = int(n[0])
n.remove(n[0])
o = []
cutx = [0, extent[0]]
cuty = [0, extent[1]]
widths = []
heights = []

for i in range(len(n)):
    o = list(map(int, n[i].split()))
    if(o[0] == 1):
        cutx.append(o[1])
    elif(o[0] == 0):
        cuty.append(o[1])
cutx.sort()
cuty.sort()

def cutLine(a, b):
    for j in range(len(a)-1):
        b.append(a[j+1] - a[j])

cutLine(cutx, widths)
cutLine(cuty,heights)
print(max(widths) * max(heights))