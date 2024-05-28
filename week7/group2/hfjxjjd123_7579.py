import sys
input = sys.stdin.readline

N, M = map(int, input().split())
capacity = list(map(int, input().split()))
cost = list(map(int, input().split()))

s = 0
for i in range(N):
    s += cost[i]

dp = [[-1]*(s+1) for _ in range(N+1)]

def dp_update(i, j, c):
    dp[i][j] = max(dp[i][j], c)

for i in range(N):
    dp_update(i+1, cost[i], capacity[i])
    for j in range(s+1):
        if dp[i][j] != -1:
            dp_update(i+1, j, dp[i][j])
            dp_update(i+1, j+cost[i], dp[i][j]+capacity[i])

for cost in range(s+1):
    tmp = dp[N][cost]
    if tmp !=-1 and tmp>= M:
        print(cost)
        break