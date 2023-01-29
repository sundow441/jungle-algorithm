from sys import stdin
stdin = open("inputfile.txt", "r")
N, M = list(map(int, stdin.readline().strip().split()))

board = [list(stdin.readline().strip()) for _ in range(M)]
# for i in board:
print(board[0][0])

directionX = [-1, 1, 0, 0]
directionY = [0, 0, -1, 1]