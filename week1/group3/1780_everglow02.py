#1780번-종이의 개수

import sys
input = sys.stdin.readline

matrix = []
N = int(input())
for i in range(N):
    matrix.append(list(map(int, input().split())))

zero = 0
one = 0
minus_one = 0

def slice(x, y, n):
    crit = matrix[x][y]
    global zero, one, minus_one

    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[i][j] != crit: # 다 똑같은 숫자가 아니라는 의미
                slice(x, y, n//3)
                slice(x, y+n//3, n//3)
                slice(x, y+2*(n//3), n//3)

                slice(x+n//3, y, n//3)
                slice(x+n//3, y+n//3, n//3)
                slice(x+n//3, y+2*(n//3), n//3)

                slice(x+2*(n//3), y, n//3)
                slice(x+2*(n//3), y+n//3, n//3)
                slice(x+2*(n//3), y+2*(n//3), n//3)
                return

    if crit == 0:
        zero += 1
    elif crit == 1:
        one += 1
    else:
        minus_one += 1

slice(0, 0, N)
print(minus_one, zero, one, sep='\n')
