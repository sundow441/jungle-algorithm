import sys

sys.stdin = open('inputfile.txt','r')
n = int(sys.stdin.readline())
a = 0

def hypen(b):
    for i in range(b * 4):
        print("_", end="")

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
def JH(max):
    global a

    hypen(a)
    print("\"재귀함수가 뭔가요?\"")
    if(a < max):
        hypen(a)
        print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        hypen(a)
        print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        hypen(a)
        print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    
    if(a == max):
        hypen(a)
        print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        for i in range(max + 1):
            hypen(a)
            print("라고 답변하였지.")
            a -= 1
        return
    a += 1
    JH(max)

JH(n)