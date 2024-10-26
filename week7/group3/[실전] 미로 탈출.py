#import sys
#input = sys.stdin.readline
from collections import deque

# maze = [
#     [1,0,1,0,1,0],
#     [1,1,1,1,1,1],
#     [0,0,0,0,0,1],
#     [1,1,1,1,1,1],
#     [1,1,1,1,1,1]
# ]
# N,M = 5,6
N, M = map(int,input().split())
maze = []
for i in range(N):
    maze.append(list(map(int,input())))

visited = [[False] * M for _ in range(N)]
# 방향키
dx = [0,1,0,-1]
dy = [-1,0,1,0]

start = [0,0,0]    # 시작 좌표, 거리
exit = [N-1,M-1] # 출구 좌표

def bfs(start):
    # 1. 현재 처리 중인 노드 확인
    # 2. 해당 노드와 인접한 노드들 큐에 집어넣고 방문 표시
    # 3. 가장 아래에 깔린 노드 탈출
    # 큐에서 다음 노드 처리 반복 
    q = deque()
    # 초기화
    q.append(start)     
    visited[0][0] = True 
    depth = 0

    while q:
        # [처리 과정]
        # 1단계
        x,y = q[0][0],q[0][1] # 현재 처리 중인 노드 위치
        depth=q[0][2]+1       # 주시 중인 노드와 인접한 노드들은 해당 노드의 거리+1이므로 미리 초기화

        if [x,y] == exit:
            print(depth)
            break
        #maze[x][y]=q[0][2]   # 결과 그래프 출력용
        #print('watching:',x,y)
        
        # 2단계
        for i in range(4): #주변부 탐색 
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M: # 범위 제한
                continue
            if visited[nx][ny]: # 방문 했던 곳이면 스킵 
                continue
            if maze[nx][ny] != 0: # 괴물이 없으면
                visited[nx][ny] = True
                q.append([nx,ny,depth]) # 그 주변 길을 계속 탐색할 가치가 있으므로 큐에 집어넣기
            #print(nx,ny,q)     # 탐색할 때마다 큐 상황 확인 용
        # 3단계
        #print()
        q.popleft()

bfs(start)

# for i in range(N):
#     print(maze[i])