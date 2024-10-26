import sys
from collections import deque 
input = sys.stdin.readline

N, L, R = map(int, input().split())
countries = []
for _ in range(N):
    countries.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 문제) 내가 탐색했을 땐 조건에 안 맞더라도 쟤가 탐색할 땐 조건에 맞을 수 있음
def BFS(sx,sy):
    next = deque([(sx,sy)])
    visited = [[False]*N for _ in range(N)]
    allied = [[False]*N for _ in range(N)]
    visited[sx][sy] = True
    friend = [] # 첫 시작점이 연합 불가한 점일 수 있으므로 비어두기

    while(next): # 큐가 비어있지 않는 경우 (= 인접한 노드가 있을 경우)
        x,y = next.popleft() # 현재 보고 있는 노드

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N: # index of error 방지
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                next.append((nx,ny))    
            if not allied[nx][ny]: # 연합 안 했다면 연합 가능한지 검토
                if (abs(countries[x][y] - countries[nx][ny]))>=L and abs(countries[x][y] - countries[nx][ny])<=R:
                    allied[nx][ny] = True
                    if not allied[x][y]:
                        allied[x][y] = True
                        friend.append((x,y))
                    friend.append((nx,ny))  # 연합에 추가
                    
    return friend

day=0
while(True):
    friends = BFS(0,0)
    #print(day,friends)
    
    if len(friends) == 0: # 혼자면
        print(day)
        break
    
    day+=1
    sum=0
    for f in friends:
        sum+=countries[f[0]][f[1]]
    result = sum//len(friends)
    for f in friends:
        countries[f[0]][f[1]]=result
    
    # for i in range(N):
    #     print(countries[i])


# 1. 국가 행렬을 순차적으로 돌면서 상하좌우 탐색 (인덱스 범위 넘어나지 않게 조심)
# 1.0 방문 시 기록, 방문 안 했으면 패스 v
# 1.1 탐색 시 연합 가능한지(인구 차이가 L명 이상 R명 이하인지) 확인
# 1.2 연합 가능하면 연합 리스트에 추가
# 1.2.1 연합 불가능한 지점을 만나면 멈추고 인구 이동 횟수 추가??
