import sys
input = sys.stdin.readline

'''
M 이상의 데이터를 확보해도 되는데, C를 최소로
-> 0부터 증가하는 C에 대하여, cost가 정확히 C일때,
최대 데이터 확보량 value 찾아서, M 이상일 떄 C 출력
-> knapsack 문제
C만큼 돌리기
    C에 대해 N개의 물건에 대해 돌리기

'''

N, V = map(int,input().split())
vlist = [0] + list(map(int, input().split())) #1부터 시작함을 맞추기 위해 [0]을 추가하기
clist = [0] + list(map(int, input().split()))
C = sum(clist)  
dp = [[0 for _ in range(C+1)] for _ in range(N+1)] #마찬가지로 1부터 시작을 맞추기 위해 +1을 해서 dp

#이후에는 평범한 knapsack 문제 해결 방식
for i in range(1, N+1):
    for j in range(C+1):
        if clist[i] <= j:
            dp[i][j] = max(vlist[i]+dp[i-1][j-clist[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# 해는 최대 value가 처음으로 M을 넘어가는 값
for i in range(C+1):
    if dp[N][i] >= V: # i라는 c에 대하여 dp[i][-1] 값이 M 넘어가는지 확인
        print(i)
        sys.exit() # 강종