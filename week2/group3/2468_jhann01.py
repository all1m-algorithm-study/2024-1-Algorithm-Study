#안전 영역
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
from collections import deque

#장마철에 물에 잠기지 않는 안전한 영역의 최대 개수 구하기
#-> 가장 촌수가 많을 때의 촌수 구하기

N = int(input()) # N X N행렬의 크기 지정
 # 땅으로 사용할 리스트
land = []
maxNum = 0
for i in range(N):
    land.append(list(map(int, input().split())))
    for j in range(N):
        if land[i][j] > maxNum:
            maxNum = land[i][j]




dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]# 이동표

def BFS(x, y, rain): #BFS정의
    queue = deque([(x, y)])
    visited[x][y] = 1 #방문한 적 있다고 표시

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            # 그리곤, 해당 좌표의 상하좌우로 함수를 재귀
            next_x = cx + dx[i]
            next_y = cy + dy[i]
            if (0 <= next_x < N) and (0 <= next_y < N) and (visited[next_x][next_y] == 0) and (land[next_x][next_y] > rain):
                visited[next_x][next_y] = 1
                queue.append((next_x, next_y))


max_safe_area = 0
for rain in range(maxNum):
    visited = [[0] * N for _ in range(N)]
    safe_area = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and land[i][j] > rain:
                BFS(i, j, rain)
                safe_area += 1
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)