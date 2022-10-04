from sys import stdin
from collections import deque

stdin = open('inputfile.txt', 'r')
N = int(stdin.readline()) # 보드의 크기(N * N)
K = int(stdin.readline()) # 사과의 개수
applePos = []
for _ in range(K):
    applePos.append(list(map(int, stdin.readline().split()))) # 사과의 위치(행, 렬)
L = int(stdin.readline()) #뱀의 방향 변환 횟수
snakeRot = deque()
for i in range(L):
    snakeRot.append(stdin.readline().split()) #뱀이 회전 할 시간과 방향 L = 왼, D = 오
    snakeRot[i][0] = int(snakeRot[i][0])
appleCnt = K # 사과 개수 카운트
sBQ = deque([[1, 1]]) # 뱀의 몸통 좌표(snakeBodyQueue)
turn = 0
sR = 1 # 현재 뱀의 방향

while True:
    body = []
    if len(sBQ) >=2:
        for i in range(1, len(sBQ)):
            body.append(sBQ[i])
    else:
        body = []
       
    turn += 1
    if sR == 0:
        sBQ.appendleft([sBQ[0][0] - 1, sBQ[0][1]])
        if sBQ[0][0] <= 0 or (len(sBQ) >= 2 and sBQ[0] in body):
            print(turn)
            break
        if sBQ[0] not in applePos:
            sBQ.pop()
        elif sBQ[0] in applePos:
            appleCnt -= 1
            applePos.remove(sBQ[0])
        if len(snakeRot) != 0 and turn == snakeRot[0][0]:
            if snakeRot[0][1] == "D":
                sR += 1
                if sR == 4:
                    sR = 0
            elif snakeRot[0][1] == "L":
                sR -= 1
                if sR == -1:
                    sR = 3
            snakeRot.popleft()
    elif sR == 1:
        sBQ.appendleft([sBQ[0][0], sBQ[0][1] + 1])
        if sBQ[0][1] > N or (len(sBQ) >= 2 and sBQ[0] in body):
            print(turn)
            break
        if sBQ[0] not in applePos:
            sBQ.pop()
        elif sBQ[0] in applePos:
            appleCnt -= 1
            applePos.remove(sBQ[0])
        if len(snakeRot) != 0 and turn == snakeRot[0][0]:
            if snakeRot[0][1] == "D":
                sR += 1
                if sR == 4:
                    sR = 0
            elif snakeRot[0][1] == "L":
                sR -= 1
                if sR == -1:
                    sR = 3
            snakeRot.popleft()
    elif sR == 2:
        sBQ.appendleft([sBQ[0][0] + 1, sBQ[0][1]])
        if sBQ[0][0] > N or (len(sBQ) >= 2 and sBQ[0] in body):
            print(turn)
            break
        if sBQ[0] not in applePos:
            sBQ.pop()
        elif sBQ[0] in applePos:
            appleCnt -= 1
            applePos.remove(sBQ[0])
        if len(snakeRot) != 0 and turn == snakeRot[0][0]:
            if snakeRot[0][1] == "D":
                sR += 1
                if sR == 4:
                    sR = 0
            elif snakeRot[0][1] == "L":
                sR -= 1
                if sR == -1:
                    sR = 3
            snakeRot.popleft()
    elif sR == 3:
        sBQ.appendleft([sBQ[0][0], sBQ[0][1] - 1])
        if sBQ[0][1] <= 0 or (len(sBQ) >= 2 and sBQ[0] in body):
            print(turn)
            break
        if sBQ[0] not in applePos:
            sBQ.pop()
        elif sBQ[0] in applePos:
            appleCnt -= 1
            applePos.remove(sBQ[0])
        if len(snakeRot) != 0 and turn == snakeRot[0][0]:
            if snakeRot[0][1] == "D":
                sR += 1
                if sR == 4:
                    sR = 0
            elif snakeRot[0][1] == "L":
                sR -= 1
                if sR == -1:
                    sR = 3
            snakeRot.popleft()
    # print("turn =", turn)
    # print(sBQ[0])
    # print(sR)
    # print(snakeRot)
    # print(sBQ)