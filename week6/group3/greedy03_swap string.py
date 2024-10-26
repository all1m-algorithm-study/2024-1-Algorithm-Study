import sys
import copy
input = sys.stdin.readline

S = list(input())
S.pop() # 개행문자 날리기
S = [int(i) for i in S]

# <<수정 -> 기준: 연속된 구간이 더 적은 거>>
# [기존]
# 0이 많은지 1이 많은지 확인
# 많은 쪽으로 맞추기 (기준 정하기)
# 기준이 아닌 숫자로 시작하는 연속되는 문자열 뒤집기 
# 기준이 아닌 숫자가 남아있는지 확인
# 남아있지않을 때까지 뒤집기 반복

#crit = 1 if S.count(1) == min(S.count(1), S.count(0)) else 0 # 바꿀 숫자
#cnt=0

def count(crit):
    cnt=0
    s = copy.deepcopy(S)
    while s.count(crit) != 0: 
        p = s.index(crit)
        while p < len(s) and s[p] == crit: # 연속된 문자열 뒤집기
            s[p] = int(not crit) # 뒤집기
            p += 1 # 옆으로 이동
        cnt += 1
    return cnt

print(min(count(0),count(1)))