from sys import stdin
stdin = open("inputfile.txt", "r")

N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
arr.sort() # 회의 시작시간 기준으로 정렬

def greedy():
    meeting = arr[0] # 가장 시작시간이 빠른 회의를 따로 변수에 초기화
    count = 1 # 시작할 회의 수 카운트
    for i in range(1, N): # 0번 회의는 meeting 변수에 있으므로 1번째 회의부터 반복
        if arr[i][0] > meeting[0]: # 다음 회의 시작시간이 늦을 때
            if arr[i][0] >= meeting[1]: # meeting 종료시간이 다음 회의 시작시간보다 빠르면
                meeting = arr[i] # meeting을 다음 회의로 변경
                count += 1 # 회의 카운트 + 1
            elif arr[i][1] <= meeting[1]: # meeting 종료시간이 다음 회의 시작시간보다 늦으면
                meeting = arr[i] # 회의 카운트를 더하지 않음
        elif meeting[0] == meeting[1]: # 예외적으로 미팅 시작시간과 종료시간이 같을 때를 고려
            meeting = arr[i]
            count += 1
    print(count)
greedy()