import sys
input = sys.stdin.readline

n, m = map(int, input().split())
balls = list(map(int, input().split()))

cnt=0
for me in range(n):
    for other in range(me,n):
        if balls[other] == balls[me]:
            continue
        else :
            cnt+=1
            #print(me,other)
print(cnt)

###
import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 무게별 볼링공 개수 카운트
weight_count = [0] * (m + 1)
for weight in balls:
    weight_count[weight] += 1

# 가능한 모든 쌍의 수 계산
result = 0
for i in range(1, m + 1):
    n -= weight_count[i]  # i 무게의 볼링공을 제외한 나머지 볼링공의 개수
    result += weight_count[i] * n  # i 무게의 볼링공과 나머지 볼링공의 쌍의 수

print(result)
