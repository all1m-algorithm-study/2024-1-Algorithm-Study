ROW, COLUMN = map(int,input().split())
table  = list()

for i in range(ROW):
    table.append(list(map(int,input().split())))


def adjacents(row, column):
    global ROW, COLUMN

    result = list()

    directions = [[1,0],[0,1], [-1,0],[0,-1]]

    for dr, dc in directions:
        r = row + dr
        c = column + dc
        if 0<=r<ROW and 0<=c<COLUMN:
            result.append([r,c])

    return result


def is_separate(table):
    global ROW, COLUMN
    visited = set()
    melt = list()

    count = 0
    for row in range(ROW):
        for column in range(COLUMN):
            if table[row][column] != 0 and (row,column) not in visited:
                count += 1
                DFS(table, visited, row, column,melt)

    if(melt):              
        for r, c, m in melt:
            if table[r][c] - m >=0:
                table[r][c] -= m
            else:
                table[r][c] = 0
    else:
        return -1
    
    if count > 1:
        return 1
    else:
        return 0
    
def DFS(table, visited, row, column, melt):
    stack = list()
    stack.append((row,column))
    while(stack):
        count = 0
        node = stack.pop()

        if node not in visited:
            current_r, current_c = node
            visited.add((current_r,current_c))

            for r, c in adjacents(current_r, current_c):
                if table[r][c] != 0: 
                    if (r,c) not in visited:
                        stack.append((r,c))
                else:
                    count +=1

            if count > 0 :
                melt.append((current_r,current_c,count))

time = 0

while(True):

    result = is_separate(table)

    if result == 1:
        break
    elif result == -1:
        time = 0
        break

    time +=1

        
print(time)




            
