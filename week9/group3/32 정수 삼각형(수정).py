import sys
input = sys.stdin.readline

n = int(input())    # 1~500
triangle = []
for _ in range(n):
    triangle.append(list(map(int,input().split())))

path=[[] for _ in range(n)]   # 모든 층의 각 정수까지의 최대값 모음
path[0] = triangle[0]
#print(path)
#[[7],[10(3+7),15(8+7)],[18(10+8),16(15+1),15(15+0)]],[20(18+2),25(18+7),20(16+4),19(15+4)],[24, 30, 27, 25, 24]]
for stair in range(1,n): # 꼭대기 아래층부터 1층까지
    for i in range(len(triangle[stair])):   # 현재 층
        cur = triangle[stair][i]
        # 최댓값 위치 찾기
        _max,max_pos=-1,-1
        for pos in [i,i-1]:
            if pos<0 or pos >= len(triangle[stair-1]):
                continue 
            # 최대값 찾는 방법으로 이용
            if triangle[stair-1][pos]>_max:
                _max = triangle[stair-1][pos]
                max_pos = pos
        path[stair].append(cur+path[stair-1][max_pos])  # 새로 갱신

for i in range(n):
    print(path[i])

print(max(path[n-1]))
"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""