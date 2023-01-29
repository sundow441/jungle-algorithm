while True:
    point = int(input("포인트입려기:"))
    if point ==0:
        break
    num = point //10
    for i in range(num):
        print('별',end="")
    print()