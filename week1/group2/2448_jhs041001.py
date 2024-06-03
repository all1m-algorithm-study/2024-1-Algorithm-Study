import math

N = int(input())
N = N // 3  
n = 0

while(N//2 != 0):
    N = N // 2
    n +=1

width = 6*(2**n) - 1
height = 3*(2**n)

array = [[' ']*width for _ in range(height)]

def draw(dot):
    global array
    x = dot[0]
    y = dot[1]

    array[y][x] = '*'

def triangle(dot, n):
    x = dot[0]
    y = dot[1]
    if n == 0:
        draw(dot)
        draw([x-1,y+1])
        draw([x+1,y+1])
        for i in range(-2, 3):
            draw([x+i, y+2])
    else:
        half_height = 3*(2**(n-1))
        quarter_width =  ((6*(2**n) - 1)+1) // 4

        triangle([x,y], n-1)
        triangle([x - quarter_width, y + half_height], n-1 )
        triangle([x + quarter_width, y + half_height], n-1 )


triangle([width // 2, 0], n)

for row in array:
    print(''.join(row))