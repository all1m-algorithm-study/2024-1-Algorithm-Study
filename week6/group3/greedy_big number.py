import sys
import copy
input = sys.stdin.readline

N, cnt, maxCnt= map(int,input().split())
arr = list(map(int,input().split())) # [map()이랑 다른 이유는 뭘까]

arr2 = copy.deepcopy(arr)
arr2.sort()
arr2.pop()

i=0
sum=0

while i != cnt:
    # 최대값이 같은 게 2개 있으면 그걸로만 다 더해도 됨
    if max(arr) == max(arr2):
        sum = max(arr)*cnt # 최댓값으로만 다 더한 결과
        i = cnt # 반복문 탈출
    else: # 최대값이 같은 게 있지 않을 경우 최대값을 일단 최대한 쓰고 
        if i%(maxCnt+1) == 0: #0->3 4->7 
            for _ in range(maxCnt):
                sum += max(arr)
                i += 1
        # 두번 째로 큰 값을 한 번 쓴 후 다시 최댓값 최대한 쓰기
        else: #3->4  7->8
            sum += max(arr2)
            i += 1

print(sum)