from collections import deque
import sys
input = sys.stdin.readline

# 상하
dy = [-1, 1, 0, 0]
# 좌우
dx = [0, 0, -1, 1]


def BFS(x, y):
    queue = deque([(x, y)])  
    visited[x][y] = True     
    seaList = []             # 빙산이 녹는 부분을 저장할 리스트 초기화

    while queue:
        x, y = queue.popleft()  # 큐에서 하나의 좌표 꺼냄
        sea = 0                 # 빙산 주변 바다 개수 초기화
        for i in range(4):      # 상하좌우를 탐색(range(4))
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 지도 범위 내
                if graph[nx][ny] == 0:       # 바다
                    sea += 1                  # 빙산 주변 바다 개수 증가
                elif graph[nx][ny] > 0 and not visited[nx][ny]:  # 빙산이면서 아직 방문하지 않은 곳
                    queue.append((nx, ny))   # 큐에 추가
                    visited[nx][ny] = True   # 방문했다고 표시
        if sea > 0:                          # 빙산 주변에 바다가 있을 때
            seaList.append((x, y, sea))      # 해당 좌표와 주변 바다 개수를 리스트에 추가
    
    # 빙산 녹는 과정
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)  # 주변 바다 개수만큼 빙산을 녹임 (0보다 값이 작아질 경우 0으로 대체 -> 0은 바다 의미)
    
    return 1  # 빙산이 존재하는 경우 1을 반환

# 입력 받기
n, m = map(int, input().split())     
graph = [list(map(int, input().split())) for _ in range(n)]  # 지도 정보

year = 0  # 빙산이 분리되는 년도 초기화

# 빙산이 존재하는 동안 반복
while True:
    visited = [[False] * m for _ in range(n)]  # 방문 여부를 나타내는 리스트 초기화
    group = 0                                   # 빙산의 덩어리 개수 초기화
    ice_exist = False                           # 빙산이 존재하는지 여부를 나타내는 변수 초기화

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:  # 빙산이면서 아직 방문하지 않은 곳이라면
                group += BFS(i, j)                    # 빙산의 덩어리 개수 증가
                ice_exist = True                       # 빙산이 존재함을 표시합니다.
    
    if group > 1:             # 빙산이 2개 이상의 덩어리로 분리되었다면
        print(year)           # 분리된 년도 출력
        break                 

    if not ice_exist:         # 빙산이 존재하지 않는다면
        print(0)              # 0 출력
        break                 

    year += 1                 # 빙산이 존재하고 분리되지 않았다면 년도 증가
