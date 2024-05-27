import sys
input = sys.stdin.readline

n, m = map(int, input().split())
monthly_candle = list(map(lambda x: abs(int(x)), input().split()))

'''
행 | 열
m | Ai
'''
# Bottom-up
def solve(a, m):
    for i in range(2, m+1):
        for j in range(1024):
            if (dp[i-1][j] == -1):
                continue

            for k in monthly_candle:
                dp[i][k^j] = k^j
    
    
    return max(dp[m])

# Ai를 index로
dp = [[-1 for _ in range(1024)] for _ in range(m+1)]

for i in monthly_candle:
    dp[0][i] = i
    dp[1][i] = i    # m = 1 일 때

print(solve(monthly_candle, m))