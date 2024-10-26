def solution(n, build_frame):
    pole = [[False]*(n+1) for _ in range(n+1)]  # 정점은 n+1개
    bow = [[False]*(n+1) for _ in range(n+1)]
    
    def checkRule1(i,j):
            # 1)바닥 혹은 다른 기둥 위에 있는지 확인
            if i == 0 or pole[i-1][j]:
                return True
            # 2)또는 어느 한쪽 보 위에 있는지 확인
            elif bow[i][j] or (i>0 and bow[i][j-1]):    # 범위 추가
                return True
            return False
    def checkRule2(i,j):
        if pole[i-1][j] or pole[i-1][j+1]:  # 한쪽 끝에 기둥과 닿아있는지
            return True
        elif i>0 and bow[i][j-1] and bow[i][j+1]:   # 양쪽 끝에 보가 있는지
            return True
        return False
    
    # 1. 공사
    for i in range(len(build_frame)):
        y,x,a,b = build_frame[i]    # 문제의 x,y는 열좌표, 행좌표를 나타냄. 따라서 바꿔서 넣어줌.
        if a == 0: # 기둥
            # 생성할 경우
            if b == 1:
                # 조건 만족할 경우 생성
                pole[x][y]=checkRule1(x,y)
            # 삭제할 경우
            else:
                cond1,cond2=False,False
                # 1)위에 기둥이 없을 경우
                if not pole[x+1][y]:
                    cond1=True    # 삭제
                # 2)위에 기둥이 있는데 해당 기둥의 양쪽에 보가 있을 경우
                elif pole[x+1][y] and checkRule1(x+1,y):  
                    cond1=True
                # 3)삭제할 기둥 위에 있는 보의 오른쪽 아래에 다른 기둥이 있거나 해당 보의 양쪽에 다른 보가 있을 경우
                # if not bow[x+1][y] or (bow[x+1][y] and checkRule2(x+1,y)):
                #     cond2=True  
                if not bow[x+1][y]:
                    cond2=True
                else:
                    pole[x][y] = False # 임시로 삭제
                    if not checkRule2(x+1,y): # 삭제했는데 안 괜찮으면 (삭제하면 안됨)
                        pole[x][y]=True # 원상복구
                    else:
                        cond2=True
                  
                if cond1 and cond2:
                    pole[x][y]=False     
            continue
        # 보
        # 생성할 경우
        if b==1:
            # 해당 점 아래에 기둥이 있거나 양 끝이 다른 보와 동시에 연결되어있는 경우
            bow[x][y]=checkRule2(x,y)
            continue
        # 삭제할 경우
        # 양쪽 보가 없으면 상관 없음
        if not bow[x][y-1] and not bow[x][y+1]:
            bow[x][y]=False
        # 양쪽 보 있으면 삭제할 경우 둘 다 잘 연결되어있는지 확인
        else:
            bow[x][y]=False # 임시로 삭제
            if not(checkRule2(x,y-1) and checkRule2(x,y+1)): # 잘 연결되어있지 않으면 원상복귀 
                bow[x][y]=True

        
    # 2. 공사 결과
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if pole[i][j]:
                answer.append([j,i,0])
            if bow[i][j]:
                answer.append([j,i,1])
    answer.sort()

    return answer

build_frame=[
    [1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],
    [5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]
]
# build_frame=[
#     [0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],
#     [1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],
#     [1,1,1,0],[2,2,0,1]
# ]
print(solution(5,build_frame))