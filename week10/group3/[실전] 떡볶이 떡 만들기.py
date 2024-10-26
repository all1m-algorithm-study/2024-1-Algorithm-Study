import sys
input = sys.stdin.readline

n,m = map(int,input().split())
rice_cake = list(map(int,input().split()))
rice_cake.sort()
# 10 15 17 19
candidates = []

def check(std):
    sum=0
    for rc in rice_cake:
        if rc>std:
            sum+=(rc-std)
    if sum < m:
        return False            # 정답 후보가 될 수 없음
    elif sum > m:
        candidates.append(std)  # 정답 후보로 추가
    else: # sum == m
        return True             # 빼박 정답 후보

def binary_search(arr):
    left = 0 # min(arr)   # 이 함수에서는 인덱스가 아니라 값을 가리킴
    right = max(arr) #-1 m의 최솟값:1

    while left<=right:
        mid = (left+right)//2

        if check(mid) == False:
            right = mid-1     # mid가 너무 컸기 때문에 줄여야 함
        elif check(mid) == True:
            return mid
        else:               # 얻은 떡이 m보다 컸음=mid가 작았기 때문에 키워야 함
            # result = mid  # 어차피 갱신되므로
            left = mid+1
    # 정확히 m이 나오지 않음=> 근사값 찾아야
    return min(candidates)
    #return result

print(binary_search(rice_cake))