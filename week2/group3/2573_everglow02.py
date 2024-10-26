import sys
import copy
from collections import deque
input = sys.stdin.readline

year = 0
chunk = 0
iceMap = []

N, M =  map(int,input().split())
for i in range(N):
 iceMap.append(list(map(int,input().split())))

zeroMatrix = [[0 for col in range(M)] for row in range(N)]
oceanMap = copy.deepcopy(zeroMatrix)

def checkSurround():
  for i in range(1,N-1):  # N-1 X M-1 칸 다 검사
    for j in range(1,M-1):
      if (iceMap[i][j+1] == 0): # 동
        oceanMap[i][j] += 1
      if (iceMap[i][j-1] == 0): # 서
        oceanMap[i][j] += 1
      if (iceMap[i-1][j] == 0): # 남
        oceanMap[i][j] += 1
      if (iceMap[i+1][j] == 0): # 북
        oceanMap[i][j] += 1

dx,dy = [-1,1,0,0], [0,0,-1,1]      
def bfs_countChunk(i,j): # 덩어리가 몇 개인지 확인하기
    q = deque()
    global chunk
    q.append((i,j))
    chunk += 1
    while q:
        x,y = q.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]  
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if iceMap[nx][ny]!=0 and visited[nx][ny]==0: #주변이 chunk이고 방문하지 않았으면
                q.append((nx,ny))
                visited[nx][ny] = chunk # 덩어리 개수 체크

def melt():
    for i in range(1,N-1):  # N-1 X M-1 칸 다 검사
        for j in range(1,M-1):
            if (iceMap[i][j] - oceanMap[i][j]>=0):
                iceMap[i][j] -= oceanMap[i][j]
            else:
                iceMap[i][j] = 0
            
            
while (chunk < 2):
    checkSurround()
    melt()  
    year += 1
    chunk = 0

    visited = copy.deepcopy(zeroMatrix)
    for i in range(N):  # N-1 X M-1 칸 다 검사
        for j in range(M):
            if visited[i][j]==0 and iceMap[i][j]>0: #방문한 적 없는 얼음있는 곳
                bfs_countChunk(i,j)  
    
    oceanMap = copy.deepcopy(zeroMatrix) #init ocean count
    
    if (iceMap == oceanMap and chunk < 2):
        print(0)
        sys.exit()
        
print(year)