import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

'''
ice 저장해놓기
ice 한 점에 대해 BFS 돌리기
    visited 갯수와 ice 갯수 다르면 두덩이 이상
    -> 그만 돌리고 날짜 반환
ice에 대해 상하좌우 확인해서 뺄거 deque에 저장
deque 풀면서 0 이하 되는 경우 0으로 바꾸기
0 이상인 경우 next_ice에 저장
next_ice = ice
'''

def melting():
    global ice
    t = 0
    while ice: #덩이수 계산 BFS
        start = next(iter(ice))
        queue = deque([start])
        visited = {start}
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (nx, ny) in ice and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        if len(visited) != len(ice):
            return t

        melt_info = deque() #얼음 녹이기
        next_ice = set()
        for x, y in ice:
            water = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if pole[nx][ny] == 0:
                    water += 1
            if water:
                melt_info.append((x, y, water))
            else:
                next_ice.add((x,y))
        
        for _ in range(len(melt_info)):
            x, y, water = melt_info.popleft()
            pole[x][y] -= water
            if pole[x][y] > 0:
                next_ice.add((x, y))
            else:
                pole[x][y] = 0

        ice = next_ice
        t += 1
    
    return 0

N, M = map(int, input().split())
pole = [list(map(int, input().split())) for _ in range(N)]

ice = set((i, j) for i in range(N) for j in range(M) if pole[i][j]) #배열 순환하면서 0 아닌거 저장

print(melting())