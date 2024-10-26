import sys
input = sys.stdin.readline

# 최소한의 화폐 개수로 특정 값의 돈 만들기
n,goal = map(int,input().split()) 
wallet = []     #길이 1~100
for _ in range(n):
    wallet.append(int(input()))
wallet.sort()
# 1원부터 goal원까지 만들 수 있는 최소 화폐 개수 테이블 dp
END = goal+1
#dp=[0]*END # 1~10000
dp=[END]*END # 1~10000
for money in wallet:    # 초기화
    if  money<END:
        dp[money] = 1

for i in range(min(wallet),END): # 최소 화폐 단위부터 의미 있음
    for money in wallet:    # 2,3
        if i+money<END:     # 범위 제한
            # result = min(dp[i+money],dp[i]+1) 
            # dp[i+money] = result if result>0 else dp[i]+1
            dp[i+money] = min(dp[i+money],dp[i]+1)
        
print(dp[goal] if dp[goal]!=END else -1)