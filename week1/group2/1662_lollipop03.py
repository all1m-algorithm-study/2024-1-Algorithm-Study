import sys
from collections import deque
input = sys.stdin.readline

'''
    뒤에서부터 ) 체크하며 값에 +1 넣기
       넣다가 )라면:
           그 바로 앞부터 다시 compression
           리턴값과 그다음 값 곱해서 +해주기
           지정한 위치로 이동하기
       넣다가 (라면
           값, 위치 반환하기
       맨 처름이라면
           값 리턴하기
'''

def compression(S):
    sum = 0
    while S:
        check = S.pop()
        if check == ')':
            subsum = compression(S)
            sum += subsum * int(S.pop())
        elif check == '(':
            return sum
        else:
            sum += 1
    return sum

S = deque(list(input().strip()))
print(compression(S))