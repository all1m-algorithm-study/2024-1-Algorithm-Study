import sys
input = sys.stdin.readline

n = int(input())
dp = [0*i for i in range(1001)]

dp[0] = 1
dp[1] = 1

def solve(i):   # dp[i]값 보여주는 함수
    if i == 0 or i == 1:
        return dp[i]
    for m in range(2,1001):
        dp[m] = dp[m-2] + dp[m-1] 
    return dp[i]

print(solve(n)%10007)