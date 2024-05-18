from collections import deque
import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline


'''
빙산이 처음부터 없는 경우
빙산이 처음부터 두 덩어리 이상인 경우
빙산의 인접 바다 갱신
빙산 remove()의 시간복잡도가 오더 N -> 딕셔너리로 변경(해시테이블)
for문 돌면서 딕셔너리 값 제거 불가 -> 남길 값만 filtered 딕셔너리에 저장
visited 초기화 부분 개선
'''

# matrix max size 300 * 300 = 90000
# icebergs max size 10000

# 좌우상하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def melting(iceberg, maps):
    filtered = dict()
    num = 0
    # print(iceberg)
    for ice_list in iceberg.values():
        # print(i, j, k)
        melt = maps[ice_list[0]][ice_list[1]] - ice_list[2]
        maps[ice_list[0]][ice_list[1]] = melt
        # if melt <= 0:
        #     iceberg.remove([i, j, k])
        if melt > 0:
            filtered[num] = [ice_list[0], ice_list[1], melt]
            num += 1

    return filtered


# 연결된 빙산
def bfs(maps, start, visited, n, m):    # start는 list로 전달 됨
    q = deque()
    start_x = start[0]
    start_y = start[1]
    q.append([start_x, start_y])
    visited[start_x][start_y] = True

    while q:
        curr = q.popleft()
        curr_x = curr[0]
        curr_y = curr[1]
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and maps[nx][ny] > 0:
                q.append([nx, ny])
                visited[nx][ny] = True

def check(maps, iceberg, visited):
    for ice_list in iceberg.values():
        if (maps[ice_list[0]][ice_list[1]] > 0):
            if (visited[ice_list[0]][ice_list[1]] == False):
                return True

    return False

def adj_sea_update(maps, iceberg, n, m):
    num = 0
    for ice_list in iceberg.values():
        sea = 0
        for j in range(4):
            nx = dx[j] + ice_list[0]
            ny = dy[j] + ice_list[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if (maps[nx][ny] <= 0):
                sea += 1
        iceberg[num] = [ice_list[0], ice_list[1], sea]   # iceberg 원본 업데이트
        num += 1

    return iceberg


def main():
    n, m = map(int, input().split()) # 행, 열
    # map
    maps = [list(map(int, input().split())) for _ in range(n)]
    # print(map)

    # 초기화
    
    '''
    행 | 열 | 인접 바다 수
    '''
    iceberg = dict()
    years = 0
    num = 0
    for x in range(n):
        for y in range(m):
            if (maps[x][y] != 0):    # 빙산을 만나면
                iceberg[num] = [x, y, 0]
                cnt = 0
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if (maps[nx][ny] == 0):
                        cnt += 1
                iceberg[num] = [x, y, cnt]
                num += 1

    visited = [[False]*m for _ in range(n)] # 초기화 부분 개선
    while(1):  
        if (len(iceberg) == 0):
            years = 0
            break        
        bfs(maps, iceberg[0], visited, n, m)
        # dfs(maps, iceberg[0][0], iceberg[0][1], visited, n, m)
        if(check(maps, iceberg, visited) == True):
            break
        for ice_list in iceberg.values():
            visited[ice_list[0]][ice_list[1]] = False
        iceberg = melting(iceberg, maps)
        adj_sea_update(maps, iceberg, n, m)
        years += 1
        # print(years)

    print(years)

if __name__ == "__main__":
    main()
