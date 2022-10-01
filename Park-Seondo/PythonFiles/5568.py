from sys import stdin
from itertools import permutations as p
import sys

sys.stdin = open('inputfile.txt', 'r')
m = sys.stdin.read().splitlines()

cards = []
n, k = int(m[0]), int(m[1]) #카드 총 개수, 뽑을 카드 수
m.remove(m[0])
m.remove(m[0])

for i in range(n): # 카드 리스트 생성
    cards.append(int(m[i]))

res = set() #set 자료형에 뽑은 카드 저장(중복되지 않음, 순서가 없음)
for j in list(p(cards,k)):
    res.add("".join(list(map(str,j)))) #저장한 카드 숫자 합치기

print(len(res))