import sys
input = sys.stdin.readline

N = int(input())
cmd = list(input().split())

def move(dir):
    x, y = 0,0
    if dir == 'L':
        y-=1
    elif dir == 'R':
        y+=1
    elif dir == 'U':
        x-=1
    elif dir == 'D':
        x+=1
    return (x,y)

posX,posY = 0,0

for i in range(len(cmd)):
    col = move(cmd[i])[0]
    row = move(cmd[i])[1]
    if col<0 or row<0 or col>=N or row>=N:
        continue
    posX+=col
    posY+=row

print(posX+1,posY+1) 

# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# cmd = ['L','R','U','D']

# for plan == cmd[i]:
#     nx = x+dx[i]
#     ny = y+dy[i]