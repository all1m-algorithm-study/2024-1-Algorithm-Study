import sys
input = sys.stdin.readline

M, K = map(int, input().split())
b_nums = []

def get_nsum(n):
    s = 0
    while n > 0:
        s += (n%10)
        n //=10
    return s

for m in range(1,M+1):
    if m % get_nsum(m) == 0:
        b_nums.append(m)
        
dp = [[0]*(M+1) for _ in range(len(b_nums))]
for i in range(M+1):
    dp[0][i] = 1
    
for j in range(1, len(b_nums)):
    b = b_nums[j]
    #1 dp[k']
    for i in range(1, M+1):
        dp[j][i] += dp[j-1][i]
        dp[j][i] %= K
    #2 whole new one
    b_tmp = b
    while b_tmp <= M:
        dp[j][b_tmp] += 1
        dp[j][b_tmp] %= K
        b_tmp += b
    #3 배수 개수만큼 추가
    b_tmp = b
    i = 0
    while b_tmp <= M:
        for k in range(b_tmp+1, M+1):
            dp[j][k] += dp[j-1][k-b_tmp]
            dp[j][k] %= K
        b_tmp += b

print(dp[-1][-1])