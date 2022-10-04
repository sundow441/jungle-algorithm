from sys import stdin

stdin = open('inputfile.txt', 'r')
n = stdin.read()
stack = []
score = 0
tmp = 1

for i in range(len(n)):
    if n[i] == "(":
        stack.append(n[i])
        tmp *= 2
    elif n[i] == "[":
        stack.append(n[i])
        tmp *= 3
    elif n[i] == ")":
        if not stack or stack[len(stack) - 1] != "(":
            score = 0
            break
        elif n[i - 1] == "(":
            score += tmp
        stack.pop()
        tmp //= 2
    elif n[i] == "]":
        if  not stack or stack[len(stack) - 1] != "[":
            score = 0
            break
        elif n[i - 1] == "[":
            score += tmp
        stack.pop()
        tmp //=3
if stack:
    score = 0
 
print(score)
# 괄호 열릴 때 stack에 괋호 append 하고 tmp에 곱해줌
# 괄호 닫힐 때 직전 괄호와 매치되면 score에 tmp 더해주고 stack에서 pop 한 뒤 tmp는 나누기
# 괄호 짝이 안맞으면 score = 0 하고 break
# for문 끝나고 stack에 남아있으면 score = 0
# score 출력