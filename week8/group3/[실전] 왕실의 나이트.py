# 왕실의 나이트
# 입력: 나이트의 현재 좌표
# 출력: 이동 가능한 위치 경우의 수
import sys
input = sys.stdin.readline

pos = list(input())
table = ['a','b','c','d','e','f','g','h']

x = int(pos[1]) # 2
y = table.index(pos[0])+1 #c
# y = int(ord(pos[0])) - int(ord('a')) + 1

dx = [2,2,1,-1,-2,-2,1,-1]
dy = [1,-1,2,2,1,-1,-2,-2]
# step = [(2,1),(2,-1),(-2,1),(-2,-1)(1,2),(-1,2),(1,-2),(-1,-2)]
count=0
for i in range(8):
# for step in steps:
    nx = x+dx[i]
    ny = y+dy[i]
    #ny = x+step[1]
    if nx<1 or ny<1 or nx>8 or ny>8: # 1,1 ~ 8,8
        continue
    count += 1
print(count)