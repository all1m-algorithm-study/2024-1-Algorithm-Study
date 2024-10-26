import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(map(int, input().split()))
    # 데이터 받을 때 미리 최솟값 비교 가능
mins = []
for i in range(N):
    mins.append(min(matrix[i]))

max(mins)

