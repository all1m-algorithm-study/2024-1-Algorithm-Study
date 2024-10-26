import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt=0
while N != 1:
    if N%K == 0:
        N /= K 
        cnt+=1
    else:
        N -= 1
        cnt+=1
# 또는 처음부터 나눠야할 횟수만 기억하고 실제로 연산하진 않기
print(cnt)    