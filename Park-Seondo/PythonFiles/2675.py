import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
testcase = int(n[0]) # 받아온 배열의 0번 인덱스에 있는 testcase를 할당

for i in range(1, testcase+1):
    m = list(n[i].split())
    chr = list(m[1])
    for j in range(len(chr)):
        for k in range(int(m[0])):
            if(j == len(chr) - 1 and k == int(m[0]) - 1):
                print(chr[j])
            else:
                print(chr[j], end='')