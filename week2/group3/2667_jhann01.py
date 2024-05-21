#단지번호붙이기
# import sys
# input = sys.stdin.readline

n = int(input())

graph = []
result = []
count = 0

for i in range(n):
    graph.append(list(map(int, input())))

#한 점을 기준으로 '위 아래 왼쪽 오른쪽' 으로 한 칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#DFS
def dfs(x, y):
    global count
    if x<0 or x>=n or y<0 or y>=n:
        return

    if graph[x][y] == 1:
        count = count + 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0
result.sort()

print(len(result))
for k in result:
    print(k)
