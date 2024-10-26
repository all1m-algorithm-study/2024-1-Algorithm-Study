import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
M = int(input())
req = list(map(int,input().split()))

def binary_search(arr,left,right,x):
    if left<=right:
        middle = (left+right)//2
        if arr[middle]<x:
            return binary_search(arr,middle+1,right,x)
        elif arr[middle]>x:
            return binary_search(arr,left,middle-1,x)
        else:
            print('yes',end=' ')
    else:
        print('no',end=' ')
    
nums.sort()

for num in req:
    binary_search(nums,0,N-1,num)