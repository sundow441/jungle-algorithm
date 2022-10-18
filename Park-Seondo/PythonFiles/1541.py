from sys import stdin

stdin = open("inputfile.txt", "r")
# - 기준으로 오른쪽을 최대한 더한 값을 왼쪽에 빼준다면 최소값이 나올 것
arr = stdin.readline().strip().split("-") # 식을 -기준으로 반으로 나눔
ans = 0
for i in arr[0].split('+'): # 왼쪽 값을 모두 더함
    ans += int(i)
for i in arr[1:]:
    for j in i.split('+'): # 오른쪽을 모두 더한 값을 왼쪽값에서 빼줌
        ans -= int(j)
print(ans)