import sys

sys.stdin = open('inputfile.txt','r')
n = sys.stdin.read().splitlines() # read만 하고 print에서 인덱스를 명시 안했을 때 런타임 에러
print(ord(n[0])) # ord : 문자를 아스키 코드 값으로 변환해줌
              # chr : 숫자에 맞는 아스키 코드로 변환해줌