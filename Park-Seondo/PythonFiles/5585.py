from sys import stdin
stdin = open("inputfile.txt", "r")

M = 1000 - int(stdin.readline())
tmp = 0

if M >= 500:
    tmp += M // 500
    M %= 500
if M >= 100:
    tmp += M // 100
    M %= 100
if M >= 50:
    tmp += M // 50
    M %= 50
if M >= 10:
    tmp += M // 10
    M %= 10
if M >= 5:
    tmp += M // 5
    M %= 5
tmp += M
print(tmp)