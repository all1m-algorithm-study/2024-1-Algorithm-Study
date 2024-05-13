import sys
input = sys.stdin.readline

n = int(input()) #NXN 행렬의 크기를 입력
paper = [list(map(int, input().split())) for _ in range(n)] #행렬 입력
minus_cnt = 0
zero_cnt = 0
plus_cnt = 0

def check(n, row, col): # 함수 정의

    global minus_cnt, zero_cnt, plus_cnt #전역변수 설정
    #해당 문제 case
    num_check = paper[row][col] # num_check = paper[0][0]
    for i in range(row, row + n): # row 0~9까지
        for j in range(col, col + n):#column 0~9까지
            if paper[i][j] != num_check: # paper[0~9][0~9] != paper[0][0]
                for k in range(3): #row에 대하여 1, 2, 3
                    for l in range(3): #column에 대하여 1, 2, 3
                        check(n//3, row + k * (n//3), col + l * (n//3))
                        #check(행렬크기=3, row=3,6,9, col = 3,6,9)로 9개로 분리 후 재귀
                return #질문 : break와 비슷한 효과를 준다는 것은 확인하였는데
                       #뭘 어디서 어디로 리턴 해주는지 의미를 모르겠습니다.

    if num_check == -1:#개수
        minus_cnt += 1
    elif num_check == 0:
        zero_cnt += 1
    elif num_check == 1:
        plus_cnt += 1

check(n, 0,0)
print(f"{minus_cnt}\n{zero_cnt}\n{plus_cnt}")#출력
