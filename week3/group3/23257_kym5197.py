#-*- coding: utf-8 -*- 

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

# 풀이 1
n, m = MIIS()
montly_bong = list(abs(x) for x in MIIS())

last_montly_bong = set(montly_bong)
for _ in range(m - 1):
    last_montly_bong = set(i ^ j for i in montly_bong for j in last_montly_bong)

print(max(last_montly_bong))

# 풀이 2
n, m = MIIS()
montly_bong = list(MIIS())
dp = [[False] * 1024 for _ in range(m)]
# 월봉값을 절댓값으로 저장 & 월봉값 있는 위치에 표시
for i in range(n):
    montly_bong[i] = abs(montly_bong[i])
    dp[0][montly_bong[i]] = True

# 2 ~ m개 선택하는 경우의 수 탐색
for i in range(1, m):
    # 각각 위치 탐색
    for bong in montly_bong:
        for j in range(1024):
            dp[i][j ^ bong] |= dp[i - 1][j]

for i in range(1023, -1, -1):
    if dp[m - 1][i]:
        print(i)
        break