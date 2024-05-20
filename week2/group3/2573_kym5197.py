#-*- coding: utf-8 -*- 

#덱 사용
import sys
from collections import deque

#N과 M을 행과 열로 받음
N, M = map(int, sys.stdin.readline().split())

#행렬을 sea라는 행렬에 넣음
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 확인해야할 논리들 체크
# 1) 인접해있는 칸 수 확인하기
# 2) 인접해있는 칸 수 만큼 녹이기
# 3) 덩어리가 몇개인지 확인하기

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 인접해있는 0 칸 수 확인하기
# 주위 4칸을 확인하기 위해 움직이는 좌표 설정
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def melt(x,y): 
    for t in range(4):
        nx = x + dx[t] #
        ny = y + dy[t] # 0~3까지 dx, dy가 움직이므로 (0,1) (0,-1) (-1,0) (1,0)를 보면서 컨트롤 할 수 있다.
        if nx<0 or ny<0 or nx>=N or ny>=M: #만약 0아래로 아니면 커져서 바깥으로 튕기면 현재 반복을 건너 뜀
            continue #현재 진행중인 t (0 1 2 3)의 반복 요소를 제껴버린다.
        if sea[nx][ny]==0: #만약 주위가 0면
            around_sea[x][y]+=1 # 그 행렬에 해당하는 around_sea 행렬을 새롭게 만들어서 카운트를 올린다, 즉, around_sea는 주위의 0을 세는 행렬임



#덩어리가 몇 개인지 확인하기
def bfs(i,j): 
    q = deque() #큐 자료구조를 사용하여 bfs 구현
    global temp #전역 변수 temp 사용(덩어리 개수 확인용)
    q.append((i,j)) #시작점 i j를 큐에 추가 
    temp += 1 #시작했으므로 기본으로 깔려있는 덩어리 1개 스타트
    
    while q: #큐가 비어있지 않는 동알 bfs 탐색
        x,y = q.popleft() #q에서 탐색할 x,y를 꺼냄
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t] #위와 같이 주위의 얼음 탐색
            if nx<0 or ny<0 or nx>=N or ny>=M: #범위 나가면 제끼고
                continue
            if sea[nx][ny]!=0 and visited[nx][ny]==0: #주위가 0이 아니고 and 한번도 방문하지 않았다면 
                q.append((nx,ny)) #q에 추가해 다음에 탐색할 수 있도록 하고
                visited[nx][ny] = temp #이어져있다는 빙하번호로 1,2이렇게 계속 표현하면 됨
                

#기본값 설정
#주위에 0이 몇개가 있는지 카운트 할 수 있는 행렬 around_sea 생성                
around_sea = [[0 for _ in range(M)] for _ in range(N)]
#초기값은 0년
year = 0


while True: #무한 루프
    temp = 0 #현재 빙산 덩어리 개수를 저장
    count = 0 # 해빙 후 남아 있는 빙산 칸의 개수를 저장하는 변수
    year += 1 # 년도 증가
    visited = [[0 for _ in range(M)] for i in range(N)] #방문 행렬 visited
    
    for i in range(N): # 바닷물 인접 개수 구하기
        for j in range(M):
            if sea[i][j] > 0:
                count += 1 # 남아있는 얼음 개수 확인
                melt(i,j) # i,j의 인접한 칸수 확인
                
    if count == 0: # 다 녹을때까지 반복문 벗어나지 못했으므로 0 출력
        print(0)
        break
    
    for i in range(N): # 인접 개수만큼 녹이기
        for j in range(M):
            if sea[i][j] > around_sea[i][j]:
                sea[i][j]-=around_sea[i][j]
                around_sea[i][j] = 0 # 녹이고 다시 초기화
            else:
                sea[i][j] = 0
                around_sea[i][j] = 0 # 녹이고 다시 초기화


    for i in range(N): # 덩어리의 개수 구하기
        for j in range(M):
            if sea[i][j]>0 and visited[i][j]==0: # 방문한적 없고, 얼음이 있으면 bfs실행하여 덩어리 확인
                bfs(i,j) # 덩어리 개수 확인 temp에
    if temp>=2:
        print(year)
        break