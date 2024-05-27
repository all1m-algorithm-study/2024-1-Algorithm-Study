#2294
#동전 2
import sys
input = sys.stdin.readline

#n가지의 동전이 있고, 가치의 합이 k가 되도록 하고싶다.
# +개수의 최소를 곁들인..

n ,k = map(int, input().split())
coin = [0]*n
for _ in range(n):
    coin[_] = int(input())

#coin 정렬
coin.sort()

dp = [10001]*(k+1)
dp[0] = 0 #0원을 만드는데 필요한 동전 개수는 0개

for i in range(1, k+1): #i를 만드는데 필요한 동전 수
    for c in coin:#coin 리스트에서
        if i < c: #만들고 싶은 i보다 동전가치 c가 더 크다면,
            break
        else:#만들고 싶은 i보다 동전가치 c가 더 작다면,
            dp[i] = min(dp[i-c]+1, dp[i])
            #dp[1] = dp[0](값:0) + 1 = 값:1
            #dp[2] = dp[1](값:1) + 1 = 값:2
            #.값:3
            #.값:4
                #case1: c = 1) dp[5] = dp[4](값:4) + 1 = 값:5
                #case2: c = 5) dp[5] = dp[0](값:0) + 1 = 값:1
if dp[k]==10001:
    print(-1)
else:
    print(dp[k])







