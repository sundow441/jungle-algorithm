import sys

sys.stdin = open('inputfile.txt','r')
n = input().split()
x, y = int(n[0]), int(n[1])
weeks = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
week = ""

day = 1
month = 1
months = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for j in range(1, len(months)):    
    for i in range(1, 366):
        if day > months[j]:
            day = 1
            j += 1
        if x == j and y == day and i <= 6:
            week = weeks[i]
        elif x == j and y == day and i >=7:
            week = weeks[i % 7]
        if week != "":
            break
        day += 1
    if week != "":
        print(week)
        break