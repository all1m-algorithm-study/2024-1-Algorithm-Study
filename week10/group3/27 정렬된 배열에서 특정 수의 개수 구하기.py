import sys
input = sys.stdin.readline

N, x = map(int, input().split())
series = list(map(int, input().split()))

def count_with(pos,n):  # x 개수 세기
    target = series[pos]
    cur = pos
    cnt = 0
    # 현재 위치로부터 앞 탐색
    while pos >= 0:
        if series[pos] < target: # series는 오름차순 정렬이기 때문에 target이 아니면 target보다 작음
            break   # 목표가 아니므로 반복문 종료
        cnt+=1
        #print('pos',pos,cnt)
        pos-=1      # 개수 세기
    # 현재 위치로부터 뒤 탐색
    pos = cur+1 # 바로 다음 수부터 탐색
    while pos < n:
        if series[pos] > target: # target이 아니면 target보다 큼
            break   # 반복문 종료
        cnt+=1
        #print('pos',pos,cnt)
        pos+=1 
    return cnt  # 목표 개수 반환

def binary_search(n,x):
    cnt = 0
    left = 0
    right = n-1
    
    while left <= right:
        mid = (left+right)//2
        
        if series[mid]>x:
            right = mid - 1
        elif series[mid]<x:
            left = mid + 1
        else: # 찾음
            return count_with(mid,n)
    return -1   # 없으면 -1 반환

print(binary_search(N,x))