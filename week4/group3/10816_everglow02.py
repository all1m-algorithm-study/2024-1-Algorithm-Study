import sys
input = sys.stdin.readline
from collections import Counter
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
guess = list(map(int, input().split()))

cards.sort()
print(cards)
count = [0] * len(guess)

def search(targetIdx, left, right):
    #print('-------',guess[targetIdx],'-------')
    # 가능한 모든 탐색을 마쳤을 때
    if left > right:
        return
    
    mid = (left+right)//2 
    #print(cards[left], cards[mid], cards[right]) 
    
    # 찾았을 때
    if cards[mid] == guess[targetIdx]: 
        p = mid
        # 중복되는 숫자의 맨 앞으로 감
        while (p>=left and cards[p]==cards[mid]): # 7 10 10
            #print(p)
            if (p-1>=left and cards[p-1]==cards[mid]): 
                p-=1
            else:
                break
        # 중복된 숫자의 맨 뒤로 감
        while (p<=right and cards[p]==cards[mid]): 
            #print(p,cards[p])
            count[targetIdx]+=1
            p+=1

        #print(count)
        return
    # 못 찾았을 때
    elif cards[mid]>guess[targetIdx]: 
        right = mid-1
        return search(targetIdx, left, right)
    else:
        left = mid+1
        return search(targetIdx, left, right)
    
for t in range(len(guess)):
    search(t, 0, len(cards)-1)

[print(c, end=" ") for c in count]

#for c in count:
#    print(c,end=' ')