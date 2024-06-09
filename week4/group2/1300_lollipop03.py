import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

"""
1~n^2에 대하여, 파라메트릭 서치 -> 이때, k번째 수가 k보다는 클 수 없음
ex) n = 3일떄,
1,2,3 -> k <= n일 경우 k, 이후의 경우는 k번쨰 수가 ㅓk(i>1)임 
2,4,6
3,6,9
즉, 이분 탐색을 한 값이 몇번째인지 알아내기 -> 파라메트릭 서치
이때, i번째 열에 대하여, mid//i를 하면 i번째 열에 몇개 있는지 알아낼 수 있음
ex) mid = 4일 경우, i = 1일 때, 3(예외처리), i = 2일때 2, i = 3일 떄, 1
이떄, i번쨰 열의 갯수가 n개이므로, 처리한 n보다 더 클 수 없음
"""
srt, end = 0, k

while srt <= end: # def parametric search
    mid = (srt+end)//2
    cnt = 0

    for i in range(1, N+1): # def solving
        cnt += min(mid//i, N) # 예외처리, line 10~

    if cnt >= k:
        ans = mid
        end = mid-1
    else:
        srt = mid + 1
print(ans)