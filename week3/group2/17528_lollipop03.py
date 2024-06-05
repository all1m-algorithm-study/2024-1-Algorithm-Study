import sys
input = sys.stdin.readline

'''
idea) 부분 최적화인 knapsack를 사용해서, 듀얼속성을 가진 물건들을 넣어주면 되는 것이 아닌가?
시간을 value이자 volume으로 정하여, 마지막 물건까지 searching 한 후, 그 최솟값 출력
a,b를 계속 forwarding 하면서 넣어주자 -> 3중배열?? 메모리 초과
해결) value와 volume가 같으면... index 자체가 value, volume 역할을 하지 않을까?
-> a값을 인덱스로, b값을 그 값으로 지정하자

knapsack의 endpoint를 sumA로, dp를 INF으로 초기화하여
최솟값으로 계속 초기화하기, dp[0][0] = 0으로 (기본조작)

마지막까지 돌았을 떄, index가 a, 값이 b이므로, 마지막 열을 순환하면서 가장 작은 값 출력
'''

n = int(input().strip())
times = []
sumA = 0
for _ in range(n):
    a, b = map(int, input().strip().split())
    times.append((a, b))
    sumA += a

INF = sumA + 1

dp = [[INF] * (sumA + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    a, b = times[i]
    for j in range(sumA + 1):
        if dp[i][j] != INF:
            dp[i + 1][j + a] = min(dp[i + 1][j + a], dp[i][j]) #a값 넣기, b값은 보존
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + b) #b값 같은 인덱스에 넣기

ans = INF
for j in range(sumA + 1):
    ans = min(ans, max(j, dp[n][j])) # j는 a값, np값은 b값, max한 후 그 미니멈 구하기

print(ans)