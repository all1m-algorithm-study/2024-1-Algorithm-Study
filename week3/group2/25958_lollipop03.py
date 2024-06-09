import sys
input = sys.stdin.readline().strip

M, K = map(int, input().split())

#예쁜 수 구하기
pn = []
for i in range(1, M+1):
    if i%sum([int(j) for j in str(i)]) == 0: 
    #자릿수를 str로 바꾸서 int list로 바꾸기, 이후 max함수로 합쳐주기
        pn.append(i) #예쁜 수 append

'''
knapsack 응용
-> 1, 2, 3, ..., i, ..., M의 부분해를 구하기
1부터 예쁜 수만큼 차이나는 이전의 dp값을 더해주면 되지 않을까...
문제) 5의 경우, 2+3와 3+2가 동시에 발생 가능
why? dp[2] contain 2, dp[3] contain 3
해결) 각각의 예쁜 수를 한번씩만 더하게 해주면 어떨까
ll dp[M+1]을 정의
dp[0] = 1
예쁜수 배열의 k에 대하여
    dp[1] += dp[0] (1) -> dp[1] = 1
    dp[2] += dp[1] (1+1) -> dp[2] = 1
    ...
    dp[M] += dp[M-1]

    dp[2] += dp[0] (2), (1+1) -> dp[2] = 2
    dp[3] += dp[1] (1+2) (1+1+1)-> dp[3] = 2
    dp[4] += dp[2] (1+1+2), (2+2), (1+1+1+1) -> dp[4] = 1
'''
dp = [1]+[0]*M #M이 0인 경우는 없지만, 경우의 수가 1이라 1로 초기화해줌
for i in pn:
    for j in range(i, M+1):
        dp[j] = (dp[j] + dp[j - i]) % K
print(dp[-1])
