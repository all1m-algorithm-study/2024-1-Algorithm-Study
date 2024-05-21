#물통(실패)
import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input().split())
#A(A리터), B(B리터) 물통은 비어있고, C물통은 가득 차있다.(C리터)
#한 물통의 물을 다른 물통으로 쏟을 수 있다.
# 한 물통이 비거나, 다른 한 물통이 가득 찰때까지..
# A물통이 비어 있을 때, C물통에 담겨 있을 수 있는 모든 물의 경우를 구하시오

list_c = [0]*C
result = []
def DFS(a, b, c):
    q = deque([0, 0, c])

    while(list_c[q[2]] == 0): #C물통이 한번도 가진적이 없는 물의 양이라면,
        for i in (6):
            if i == 6:
                q[1] = q[1] + q[0]
            #A -> B, A -> C, B -> C, C -> B, C -> A, B -> A


        if (q[0] == 0 and q[2] != 0):#A물통이 텅, C물통이 비어있지 않다면,
            result.append(q[2])#그때 C물통의 물 양을 result에 기억
            list_c[q[2]] = 1 #C컵의 물 양을 중복되지 않게 바꾸기
            return