import sys
from collections import deque
field = []
latest = 0

#꼭 visited 리스트에 방문한 노드를 저장하고 매번 조회할 필요는 없다.
#직접 2차원 배열에 방문한 노드들을 표시하면 좌표를 아는한 바로 O(1)로 방문했는지 안했는지 확인할 수 있으니까

def look_around(point, need_visited, field,depth_field, row, column):
    global latest
    neighbor = []
    if point[0] > 0:
        neighbor.append([point[0]-1, point[1]])
    if point[0] < row-1:
        neighbor.append([point[0]+1, point[1]])
    if point[1] > 0:
        neighbor.append([point[0], point[1]-1])
    if point[1] < column-1:
        neighbor.append([point[0], point[1] + 1])

    for n in neighbor:
        if field[n[0]][n[1]] == 0 :
            need_visited.append(n)

            depth_field[n[0]][n[1]] = depth_field[point[0]][point[1]] + 1
            field[n[0]][n[1]] = 1

            latest = depth_field[n[0]][n[1]]

def check_all(field):
    for row in field:
        for point in row:
            if point == 0:
                return False
    return True


if __name__ == '__main__':
    count = 0
    need_visited = deque()
    column, row = map(int,input().split()) 
    depth_field = [[0]* column for _ in range(row)]


    for i in range(row):
        field.append(list(map(int,sys.stdin.readline().split())))
    
    #initial scan
    for r in range(row):
        for c in range(column):
            if field[r][c] == 1:
                need_visited.append([r,c])
                
    
    while need_visited:
        current = need_visited.popleft()
        look_around(current,need_visited,field,depth_field, row, column)



    
    if check_all(field):
        print(latest)
    else:
        print(-1)
