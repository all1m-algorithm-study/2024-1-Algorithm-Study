import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수
grade = [[] for _ in range(T)]

N = []
for i in range(T):
    N.append(int(input())) # 지원자 숫자
    for _ in range(N[i]):
        grade[i].append(list(map(int,input().split()))) 


for i in range(T):
    paper = sorted(grade[i])
    interview= sorted(grade[i],key=lambda x:x[1])

    next = interview
    winner = []

    for j in range(N[i]):
        std = paper[j]
        if next.count(std)>0:
            winner.append(std)
            next = interview[0:interview.index(std)+1]
            print(next, winner)

    print(len(winner))

