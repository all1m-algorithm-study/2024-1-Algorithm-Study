#12865
#평범한 배낭
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) #물품 수, 버틸 수 있는 무게

luggage = [list(map(int, input().split())) for _ in range(N)]
# [무게, 가치]
luggage.sort()
# print(luggage)

dp = [0]*(K+1) #무게 리스트

dp[0] = 0 # 0kg의 무게로 만들 수 있는 행복

# 모든 물건에 대해 반복
for weight, value in luggage:
    # dp 배열을 역순으로 반복하여 동일한 물건이 여러 번 사용되는 것을 방지
    for i in range(K, weight - 1, -1): #8부터 2까지, 3까지, 5까지.. 1씩 감소하면서 반복
        dp[i] = max(dp[i], dp[i - weight] + value)
        # case1
        # dp[7] # dp[7](값:0), dp[7-3](값:0) + 6 -> 6
        # dp[6] # dp[6](값:0), dp[6-3](값:0) + 6 -> 6
        # dp[5] # dp[5](값:0), dp[5-3](값:0) + 6 -> 6
        # dp[4] # dp[4](값:0), dp[4-3](값:0) + 6 -> 6
        # dp[3] # dp[3](값:0), dp[3-3](값:0) + 6 -> 6

        # case2
        # dp[7] # dp[7](값:6), dp[7-4](값:6) + 8 -> 14
        # dp[6] # dp[6](값:6), dp[6-4](값:0) + 8 -> 6
        # dp[5] # dp[5](값:6), dp[5-4](값:0) + 8 -> 6
        # dp[4] # dp[4](값:6), dp[4-4](값:0) + 8 -> 6

        # case3
        # dp[7] # dp[7](값:14), dp[7-5](값:0) + 8 -> 14
        # dp[6] # dp[6](값:6), dp[6-5](값:0) + 8 -> 8
        # dp[5] # dp[5](값:6), dp[5-5](값:0) + 8 -> 8


print(max(dp))

