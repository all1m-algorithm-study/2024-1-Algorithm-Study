import sys
input = sys.stdin.readline

meeting = [[0,0,0]] # 더미
N = int(input())
for _ in range(N):
    meeting.append(list(map(int, input().split()))) 

DP = dp = [0*i for i in range(N+1)] # DP[i] = i번째 회의까지 회의 인원의 최대 합
DP[1] = meeting[1][2]

for i in range(2,N+1):
    DP[i] = max(DP[i-1], meeting[i][2]+DP[i-2])

print(DP[N])

# 예시
"""
DP[1] = meeting[1][2]
DP[2] = max(DP[1], meeting[2][2])
DP[3] = max(DP[2], meeting[3][2]+DP[1]) # meeting[3][2] + meeting[1][2]
DP[4] = max(DP[3], meeting[4][2]+DP[2])
DP[5] = max(DP[4], meeting[5][2]+DP[3])
DP[6] = max(DP[5], meeting[6][2]+DP[4])
"""
# => DP[i] = max(DP[i-1], meeting[i][2]+DP[i-2])
# DP는 점화식... 머리에 새겨두자 흑흑

# k번째 회의 다음 회의는 k+2번째 회의부터 고를 수 있음