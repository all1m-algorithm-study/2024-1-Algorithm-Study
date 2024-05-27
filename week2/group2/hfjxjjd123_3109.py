import sys
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = []

nxt = [-1, 0, 1]
cnt = 0
def forward(r, c):
    global cnt
    matrix[r][c] = 'x'
    
    if c == C-1:
        cnt += 1
        return True
    
    for i in nxt:
        if r+i>=0 and r+i < R and matrix[r+i][c+1] != 'x':
            rst = forward(r+i,c+1)
            if rst:
                return True
    # matrix[r][c] = '.'
    return False

for _ in range(R):
    matrix.append(list(input().strip()))

for r in range(R):
    forward(r, 0)

print(cnt)
        