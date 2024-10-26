import sys
input = sys.stdin.readline

N, M = map(int,input().split())

ice = []
for i in range(N):
    ice.append(list(input())) #list(map(int,input())) # sys.stdin.readline으로 안 했을 때
    ice[i].pop() # 개행 문자 날리기 안 그러면 ['1','0','1','1','\n'] 이런 식

visited = [[False]*M for _ in range(N)] # 2차원 방문 배열

dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 연결된 0인 노드만 방문하는 함수 dfs
def dfs(x, y):
    global cnt0
     # 구멍 뚫린 부분(0인 부분)만 방문
    if ice[x][y] == '1':
        return
    visited[x][y] = True
    #print('here',x,y, visited[x][y])
    cnt0+=1 # 방문한 0개수(서로 연결된 부분만) 더하기
    # 주변부 탐색
    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M: #탐색 범위 제한
            continue
        if not visited[nx][ny]: #방문 안한 곳만 탐색
            dfs(nx,ny)

icecream = 0
# ahems
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cnt0=0 #초기화
            dfs(i,j)

            if cnt0>0: #dfs로는 연결된 0만 탐색하므로 dfs내에서 센 0개수가 하나 이상 존재하면 덩어리가 존재한단 뜻
                icecream+=1

print(icecream)
