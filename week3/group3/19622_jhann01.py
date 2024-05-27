#19622
#회의실 배정 3
import sys
# sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
#from collections import deque

#서준씨는 정말 부럽게도 N개의 회의와 1개의 회의실을 선물로 받았다.
#가장 효율적으로 N개의 회의를 하기 위한 최대 인원을 구하자.

N = int(input()) # 회의 수 N
Conference = [list(map(int, input().split())) for _ in range(N)]
# 회의 시작시간 , 회의 종료시간, 회의 인원

#오름차순 정렬
Conference.sort()

dp = [0] * N # 회의의 수와 동일한 dp생성
dp[0] = Conference[0][2]#dp의 첫 행은 Conference 첫 회의의 인원

for i in range(1, N): #점화식
  dp[i] = max(dp[i - 1], dp[i - 2] + Conference[i][2])
  #dp[i]는 dp[i-1]과 dp[i-2] + Conference의 i번째 회의의 인원을 더한 것 중 더 큰 것을 선택
  #예)
  # dp[1] = dp[0](값:80) 과 dp[-1](값:0) + 2번째 회의 인원(값:60) -> 80선택
  # dp[2] = dp[1](값:80) 과 dp[0](값:80) + 3번째 회의 인원(값:70) -> 150선택
  # dp[3] = dp[2](값:150) 과 dp[1](값:80) + 4번째 회의 인원(값:100) -> 180선택
  # dp[4] = dp[3](값:180) 과 dp[2](값:150) + 5번째 회의 인원(값:40) -> 190선택
  # dp[5] = dp[4](값:190) 과 dp[3](값:180) + 6번째 회의 인원(값:50) -> 230선택
  #dp[5] = 230

    #도대체 도데채 도뎨챼가 이 생각을 어떻게 하는 지를 모르겠다. 뭔가 대충 맞아가는데
    #어디서 이 발상이 떠오른거지..?

print(dp[N-1])

