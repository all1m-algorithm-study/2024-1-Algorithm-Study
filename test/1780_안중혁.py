import sys
# input = sys.stdin.readline

n = int(input()) #NXN 행렬의 크기를 입력
video = []
for i in range(n):
    video.append(list(map(int, input())))


def check(row, col, n):
    list_check = video[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if video[i][j] != list_check:
                print('(', end='')
                for k in range(2):
                    for l in range(2):
                        check(row + k*n//2, col + l*n//2, n//2)
                print(')', end='')
                return

    if list_check == 0:
        print(0, end='')
    elif list_check == 1:
        print(1, end='')

check(0, 0, n)
