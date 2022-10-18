from sys import stdin
stdin = open("inputfile.txt", "r")

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline()) # 지원자 수
    arr = [list(map(int, stdin.readline().split())) for _ in range(N)] # (서류 성적, 면접 성적) 리스트
    sortedArr = sorted(arr) # 서류 성적순으로 정렬
    topInterviewResult = 0 # 인터뷰 성적 1등 인덱스
    count = 1 # 합격 가능한 사람 수 카운트
    for i in range(1, N):
        if sortedArr[i][1] < sortedArr[topInterviewResult][1]: # 현재 까지 인터뷰 1등의 등수보다 더 높다면(숫자가 작다면)
            count += 1 # 카운트 + 1
            topInterviewResult = i # 면접 1등을 i번째로 변경
    print(count)