import sys

sys.stdin = open('inputfile.txt','r')
n = int(sys.stdin.readline()) # 단어의 개수

word = []
for i in range(n):  # 배열에 단어를 담음
    word.append(input())
words = list(set(word)) #set을 사용해 중복을 제거하고 list에 담음

sort_words = []
for i in words:
    sort_words.append((len(i), i))  #(word의 길이, word)로 묶어서 저장

result = sorted(sort_words) # sorted로 순서 정렬

for len_word, word in result: #(len(word), word)로 저장 되어 있으므로 word만 따로 출력
    print(word)