import sys
input = sys.stdin.readline

N, C = map(int, input().split())
Nlist = list(int(input()) for i in range(N))
Nlist.sort()

'''
공유기 설치 위치간 거리에 대해 파라메트릭 서치
이때, 그 거리는 min값이므로,
맨 처름부터 공유기 철치하면서, mid값에 없는 경우 그 다음 값에다 설치, 반복
만약 설치 공유기 갯수가 지정값보다 작다면: mid = min
else: max = min (더 적게 하면서 지정값이 나오는 경우가 있을 수 있으므로) 
'''

min = 1
max = Nlist[-1] - Nlist[0]
ans = 0

while min<=max: # def parametric search
    mid = (min+max)//2
    cur = Nlist[0]
    cnt = 1

    for i in range(1, len(Nlist)): # def solving
        if Nlist[i]>= mid+cur:
            cnt += 1
            cur = Nlist[i]
            
    if cnt >= C:
        min = mid + 1
        ans = mid
    else:
        max = mid - 1

print(ans)
