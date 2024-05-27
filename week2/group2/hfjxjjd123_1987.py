import sys
input = sys.stdin.readline

# Initialize the board and direction vectors
board = []
udlr = [(0, -1), (0, 1), (-1, 0), (1, 0)]
R, C = map(int, input().split())
for _ in range(R):
    board.append(list(input().strip()))

visited = [False] * 26

def dfs(r, c, cnt):
    global max_cnt
    index = alph_to_index(board[r][c])
    if visited[index]:
        return

    visited[index] = True
    cnt += 1
    max_cnt = max(max_cnt, cnt)

    for d in udlr:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < R and 0 <= nc < C and not visited[alph_to_index(board[nr][nc])]:
            dfs(nr, nc, cnt)
    visited[index] = False
    cnt -= 1

def alph_to_index(c):
    return ord(c) - ord('A')

max_cnt = 0
dfs(0, 0, 0)
print(max_cnt)