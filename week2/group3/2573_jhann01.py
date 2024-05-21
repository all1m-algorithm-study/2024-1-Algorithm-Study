#빙산
import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
from collections import deque

#상하 좌우로 바닷물이 닿아있으면 녹는 구조.


N, M = map(int, input().split()) # N X N행렬의 크기 지정
 # 빙산으로 사용할 리스트
Ice = []
for i in range(N):
    Ice.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]# 이동표

def BFS(x, y): #BFS정의
    queue = deque([(x, y)])
    visited[x][y] = 1 #방문한 적 있다고 표시

    while queue:
        cx, cy = queue.popleft()
        for j in range(4):
            # 그리곤, 해당 좌표의 상하좌우로 함수를 재귀
            next_x = cx + dx[j]
            next_y = cy + dy[j]

            if (0 <= next_x < N) and (0 <= next_y < M) and (visited[next_x][next_y] == 0):
                if Ice[next_x][next_y] > 0:
                    visited[next_x][next_y] = 1
                    queue.append((next_x, next_y))
                elif Ice[next_x][next_y] <= 0:
                    Heated[cx][cy] += 1


Time = 0
Ice_num_list = []

while True:
    visited = [[0] * M for _ in range(N)]
    Heated = [[0] * M for _ in range(N)]
    Ice_num = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and Ice[i][j] > 0:
                BFS(i, j)
                Ice_num += 1
    if Ice_num >= 2:
        break
    if Ice_num == 0:
        Time = 0
        break

    #Ice에서 Heart 빼기
    Time += 1
    for i in range(N):
        for j in range(M):
            if Heated[i][j] > 0 and Ice[i][j] > 0:
                Ice[i][j] = max(Ice[i][j] - Heated[i][j], 0)

print(Time)