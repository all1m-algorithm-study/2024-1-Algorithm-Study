import sys
from collections import deque
input = sys.stdin.readline

'''
BFS로 상하좌우 0인거 1로 바꿔주기
0이 있다면 -1 출력
아니라면 날짜 출력
'''

def bfs(starts):
    queue = deque(starts)
    checked = set(starts)
    max_day = 0
    while queue:
        i, j, day = queue.popleft()
        go = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for k in go:
            l, m = k
            if 0 <= l < N and 0 <= m < M and (l, m, day+1) not in checked and tlist[l][m] == 0:
                queue.append((l, m, day+1))
                checked.add((l, m, day+1))
                tlist[l][m] = 1
                max_day = max(max_day, day+1)
    return max_day

M, N = map(int, input().split())
tlist = [list(map(int, input().split())) for i in range(N)]

starts = [(i, j, 0) for i in range(N) for j in range(M) if tlist[i][j] == 1]

max_day = bfs(starts)

if any(0 in row for row in tlist):
    print(-1)
else:
    print(max_day)