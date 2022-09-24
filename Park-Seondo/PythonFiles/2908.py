import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
a = list(n[0].split()) # 입력받은 숫자를 받기 위한 리스트
reverseNum = "" # 거꾸로 나열한 문자를 정수로 합쳐 받을 변수
arr = [0] * len(a) # 거꾸로 나열한 정수를 최종적으로 받을 배열
reverseChar = [0] * len(list(a[0])) # 거꾸로 나열한 문자를 받을 배열

for i in range(len(a)):
    nums = list(a[i])
    for j in range(len(reverseChar)):
        reverseChar[len(reverseChar)-1-j] = nums[j]

    for k in range(len(reverseChar)):
        reverseNum = reverseNum + reverseChar[k]
        if(k + 1 == len(reverseChar)):
            arr[i] = int(reverseNum)
            reverseNum = ""
if(arr[0] < arr[1]):
    print(arr[1])
else:
    print(arr[0])