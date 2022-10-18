from sys import stdin
stdin = open("inputfile.txt", "r")

N = int(stdin.readline())
alphabet = {"A" : 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0, "G" : 0, "H" : 0, "I" : 0, "J" : 0, "K" : 0, "L" : 0, "M" : 0, 
            "N" : 0, "O" : 0, "P" : 0, "Q" : 0, "R" : 0, "S" : 0, "T" : 0, "U" : 0, "V" : 0, "W" : 0, "X" : 0, "Y" : 0, "Z" : 0}

word = [list(stdin.readline().strip()) for _ in range(N)]
arr = []
for j in range(N):
    for i in range(len(word[j])):
        alphabet[word[j][i]] += 10 ** (len(word[j]) - i - 1)
for i in alphabet.values():
    if i != 0:
        arr.append(i)
arr = sorted(arr, reverse=True)
a = 9
ans = 0
for k in range(len(arr)):
    ans += arr[k] * (a - k)
print(ans)