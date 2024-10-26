# 게임 개발

# 1. 현재 방향 기준으로 왼쪽 방향 (반시계 방향으로 90도 회전한 방향)부터 차례때로 갈 곳 정한다
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음
# 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다
# 3. 만약 네 방향 다 가본 칸이거나 바다로 되어있는 칸인 경우, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
# 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다
# 캐릭터가 이동한 칸 수 출력

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
A,B,d = map(int,input().split()) #(A,B)는 항상 육지
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split()))) # 0: 육지, 1: 바다, 맵의 외곽은 항상 바다

dir = [(-1,0),(0,1),(1,0),(0,-1)] # 북,동,남,서

def rotate(curDir):
    # if curDir == 0: #북
    #     return 3    #서
    # return curDir-1
    return (curDir - 1) % 4

visited = [[False]*m for _ in range(n)]
visited[A][B] = True
def bfs(start):
    q = deque([start])
    # 초기화
    cnt=1   #  시작 지점도 방문한 칸 수에 포함

    while q:
        x,y,cur= q.popleft() 
        #prevQ = q   # 탐색 전 큐 상태 저장
        found_new_place = False
        for _ in range(4):
            newDir = rotate(cur)    # 1. 임시 회전
            nx = dir[newDir][0]+x
            ny = dir[newDir][1]+y
            #2.1 안 가본 칸 있으면 왼쪽 방향으로 회전/전진
            if 0 <= nx < n and 0 <= ny < m  and not visited[nx][ny] and matrix[nx][ny]==0: # 범위 제한 추가
                q.append((nx,ny,newDir))
                visited[nx][ny] = True
                cnt+=1
                found_new_place = True
                break
            # 2.2 (else) 회전만 수행 
            cur =  newDir #수정) rotate(newDir)   
        #if q == prevQ:          # 3. 네 방향 다 돌았는데도 큐에 추가된 게 없으면
        if not found_new_place:
            nx = x-dir[cur][0]    # 방향 유지한 채 한 칸 뒤로
            ny = y-dir[cur][1]    # 수정) x,y 추가
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0: # 수정) 범위제한 추가
                #x=nx
                #y=ny
                q.append((nx, ny, cur))
            else:   # 바다로 막힌 경우
                break

    print(cnt)

bfs((A,B,d))

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1