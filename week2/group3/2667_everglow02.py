import sys
input = sys.stdin.readline

N = int(input())
town = [list(map(int, input().strip())) for _ in range(N)]

#for i in range(N):
#  print(town[i])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(x,y):
    global count
    if x<0 or x>=N or y<0 or y>=N: # index of error 방지
        return #False
   
    if town[x][y] == 1: # 집인지 검사
        count += 1      # 집이면 수 세기
        town[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx,ny)
        return True
    return False

"""    
for hp in houses:
   x = hp[0]
   y = hp[1]
   for dx,dy in key:
    if (town[x+dx][y+dy] == 1):
        adj.append([dx,dy])
"""

count = 0
cmplxNum = 0 # 단지 수
houseCnt = [] # 단지 내 집 수 리스트

# 그래프의 원소가 1일 때만 DFS로 집 방문
for i in range(N):
    for j in range(N):
        if DFS(i,j) == True:
            houseCnt.append(count)
            cmplxNum += 1
            count = 0

houseCnt.sort() # 오름차순 정렬
print(cmplxNum) # 총 단지 수 출력
for i in range(len(houseCnt)):
    print(houseCnt[i]) # 단지 내 집 수 출력
