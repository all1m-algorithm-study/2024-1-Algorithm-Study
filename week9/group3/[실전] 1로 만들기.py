X = int(input())
END = 30001
dp = [0]*END
dp[1]=0
# 1부터 5배수,3배수,2배수, 1더한 값 계산(거꾸로 계산)해서 DP테이블 채워나가기
# dp[n]이 0이 아니면 계산이 이루어졌단 소리이므로 값을 갱신할 필요가 없음 << 아님!
# e.g. 26
# 1 4 12 13 26 / 1 5 25 26 => 2가지 방법으로 도달 가능. 따라서 더 연산 작은 쪽으로 ㄱㄱ
# 초기엔 dp[n]이 다 0
def oper(x):
    if 5*x<END:
        dp[5*x] = dp[x]+1 if dp[5*x]==0 else min(dp[5*x],dp[x]+1)
    if 3*x<END:
        dp[3*x] = dp[x]+1 if dp[3*x]==0 else min(dp[3*x],dp[x]+1)
    if 2*x<END:
        dp[2*x] = dp[x]+1 if dp[2*x]==0 else min(dp[2*x],dp[x]+1)
    if x+1<END:
        dp[x+1] = dp[x]+1 if dp[x+1]==0 else min(dp[x+1],dp[x]+1)
    return 
# 답안 예시 => 문제 연산대로 해서 범위제한을 할 필요가 없었음. n=min함수 쓰는 건 같음
for i in range(1,END):
    oper(i)
print(dp[X])