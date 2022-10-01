import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines()
testcase = int(n[0])
n.remove(n[0])
n = list(map(int, n))

def isPrime(num):                               # 소수 판별 함수
    if num == 1:                                # 1은 소수가 아니므로 False
        return False
    for i in range(2, int(num**0.5) + 1):       # 2부터 num의 제곱근 까지
        if num % i == 0:
            return False
    return True

for i in range(testcase):                       # i 부터 testcase까지
    big, small = int(n[i]) // 2, int(n[i]) // 2 # 입력된 수를 이등분 해서 따로 담음
    for j in range(n[i] // 2):
        if isPrime(big) and isPrime(small):        # 각각의 수가 소수인지 확인
            print(small, big)                       # 소수라면 프린트
            break
        else:                                       # 소수가 아니라면 +1, -1
            big += 1
            small -= 1