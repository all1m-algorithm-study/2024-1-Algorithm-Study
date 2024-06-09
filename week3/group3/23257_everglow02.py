n,m = map(int,input().split())
arr = list(map(int,input().split()))
this_month = []

# this_month 배열에 입력받은 값을 절댓값을 취해 넣어준다.
for item in arr:
	this_month.append(abs(item))

# month라는 이름의 Set을 만든다.
# 이때 month는 1개월차의 결과(중복을 허용해 1개를 고른 경우)를 의미한다.
month = set(this_month)

# bitwise XOR 연산을 M-1번 반복한다.
# K개월의 연산 결과 = K-1개월의 연산 결과에 이번 달 연산한 값
# this_month = 연산하는 테이블의 0행이자 N개의 월봉 배열
# month = 연산하는 테이블의 0열이자 N개의 월봉 중 M개 골라 bitwise XOR 연산한 값들
for _ in range(m-1):
	month = set(i^j for i in this_month for j in month)


# 출력
print(max(month))