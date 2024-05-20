from collections import deque

n,m=map(int,input().split())

graph=[]
next=deque()  #해당하는 빙하만 넣는 큐@
for i in range(n):
  graph.append(list(map(int,input().split())))
  #graph 중에 0이 아닌 것만 next에 담음
  for j in range(m):
    if graph[i][j]!=0:
      next.append((i,j,graph[i][j]))

#방향벡터
dx=[0,1,0,-1]
dy=[1,0,-1,0]


#bfs 빙하의 4방향을 살피고 count를 0의 개수만큼 빼준다
#1년 단위의 빙하 변화 실행
def bfs():
  q=deque()
  delete=[]
  #next의 값을 꺼내 q에 넣기
  while next:
    x,y,count=next.popleft()
    q.append((x,y,count))

  #q가 빌 때까지
  while q:
    x,y,count=q.popleft()
  
    for i in range(4):
      nx,ny=x+dx[i],y+dy[i]
      if not(0<=nx<n and 0<=ny<m):
        continue
      #0일 때 count 줄임
      if graph[nx][ny]==0:
        count-=1
        #count0이면 graph[x][y]갱신 
      if count==0:
        delete.append((x,y))
        break
    #count가 0보다 큰 것만 next에 담기
    #q에 담으면 1년마다 덩어리 수 확인하기 어려우므로 next 활용
    if count>0:
      next.append((x,y,count)) 
  for i,j in delete:
    graph[i][j]=0

    
#빙하 덩어리 분리
def bfs2(x,y):
  queue=deque([(x,y)])
  visited[x][y]=True

  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx,ny=x+dx[i],y+dy[i]
      if not(0<=nx<n and 0<=ny<m):
        continue
      if visited[nx][ny] or graph[nx][ny]==0:
        continue
      queue.append((nx,ny))
      visited[nx][ny]=True


years=0    #시간
#next가 빌 때까지
while next:
  ice_count=0  #덩어리 수 1년마다 초기화
  visited=[[False]*(m) for _ in range(n)] #visited 갱신

  #빙하 덩어리 수 세기
  for i in next:
    x,y,count=i
    #next에서 꺼낸 좌표중 미방문인 것만
    if not visited[x][y]:
      bfs2(x,y)   #덩어리 분리
      ice_count+=1
  #2개 이상으로 나눠지면 종료
  if ice_count>1:
    break

  years+=1  #bfs 시행할 때마다 1년 추가
  bfs()
  
  
if ice_count>1:
  print(years)
else:
  print(0)