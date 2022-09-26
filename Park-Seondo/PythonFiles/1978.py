import sys
import math

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
testcase = int(n[0])
nums = list(map(int, n[1].split()))
primeNumCount = 0
primeNumArr = []
a = [] # 32까지의 소수를 담을 리스트

# 1000의 제곱근이 대략 32이므로 32까지의 소수를 구함
for i in range(1, 33):
    if(i == 2 or i == 3 or i == 5 or i == 7):
        a.append(i)
    elif(i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i != 1):
        a.append(i)

for j in range(len(nums)):
    for k in range(len(a)):
        if(math.sqrt(nums[j]) >= a[k] and nums[j] % a[k] == 0 or nums[j] == 1):
            break
    else:
        primeNumCount += 1
        primeNumArr.append(nums[j])

print(primeNumCount)
print(primeNumArr)