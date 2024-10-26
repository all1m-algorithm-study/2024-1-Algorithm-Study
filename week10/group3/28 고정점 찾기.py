import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

def binary_search():
    left = 0
    right = N-1

    while left<=right:
        mid = (left+right)//2

        if mid==arr[mid]:
            return mid
        elif mid<arr[mid]: # mid 오른쪽도 인덱스보다 원소가 더 클게 분명하기 때문에 오른쪽은 제외하고 왼쪽으로 가야 함
            right = mid-1
        else: # mid < arr[mid]
            left = mid+1
    return -1

print(binary_search())