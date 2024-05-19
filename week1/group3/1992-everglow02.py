#1992번-쿼드트리

import sys
input = sys.stdin.readline

image = []
N = int(input())
for i in range(N):
    image.append(list(input()))

def checkColor(i, j, n):
    color = image[i][j] # 대표값

    for x in range(i,i+n):
        for y in range(j,j+n):
            if color != image[x][y]: # 대표값이랑 같지 않으면 압축 불가! 나누기
                print('(', end="")
                checkColor(i, j, n//2) # 왼쪽 위
                checkColor(i, j+n//2, n//2) # 오른쪽 위   
                checkColor(i+n//2, j, n//2) # 왼쪽 아래                          
                checkColor(i+n//2, j+n//2, n//2) # 오른쪽 아래
                print(')', end="")
                return
    print(color, end="")
    return

checkColor(0, 0, N)
