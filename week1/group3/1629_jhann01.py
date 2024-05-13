import sys
input = sys.stdin.readline

def comb(n, m, start, selected):
    if len(selected) == m:
        print(*selected)
    elif start <= n:
        selected.append(start)
        comb(n, m, start+1, selected)
        selected.pop()
        comb(n, m, start+1, selected)

n, m = map(int, input().split())
comb(n, m, 1, [])