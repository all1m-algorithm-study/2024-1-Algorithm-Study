import sys
input = sys.stdin.readline

#n = int(input())
n=5
# 정수 n이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 구하기
# ab분 cd초
# a,c <= 5
# b,d <= 9
# 진짜 시계를 만든다..?
a,b,c,d=0,0,0,0
cnt = 0

for hour in range(n+1):
    for a in range(6):
        for b in range(10):
            for c in range(6):
                for d in range(10):
                    if hour == 3 or a == 3 or b == 3 or c == 3 or d==3:
                        cnt += 1
            
print(cnt)

# 답안 예시 : 문자열로 바꿔서 검사
"""
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt+=1
print(cnt)
"""