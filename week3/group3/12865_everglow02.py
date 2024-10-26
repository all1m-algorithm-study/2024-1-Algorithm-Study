import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0]*(K+1)
bag = []

for _ in range(N):
    W, V = map(int, input().split())
    bag.append((W,V)) 

for thing in bag:
    W, V = thing
    for i in range(K,W-1,-1):
        dp[i] = max(dp[i], dp[i-W]+V) 

print(dp[-1])
