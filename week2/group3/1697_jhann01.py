#숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

#수평선 위에서 
n, k = map(int, input().split()) #N : 수빈이가 있는 위치, K : 동생이 있는 위치
#수빈이는 순간이동 가능
#if 수빈이가 X에 위치할 경우, 1초 뒤에 앞위로 이동 or 순간이동 할 경우 (2*거리)로 이동
#수빈이는 몇초 만에 동생을 찾을 수 있을까?

max = 10 ** 5 + 1
time_table = [0] * (max)


def DFS(n):

    q = deque([n])
    while q:
        n = q.popleft()
        if n == k:
            return time_table[n]
        for next_n in (n+1, n-1, 2*n):
            if 0 <= next_n < max and time_table[next_n] == 0:
                time_table[next_n] = time_table[n] + 1
                q.append(next_n)

print(DFS(n))
