import sys
input = sys.stdin.readline

N = int(input())
print(2**N - 1)

'''
N개 하노이
    1개라면 그냥 시작에서 끝으로 옮기기
    N-1개를 처음에서 중간으로 하노이
    -> 중간과 끝이 바뀌는 하노이
    처음 끝으로 옮기기
    N-1개를 중간에서 끝으로 하노이
    -> 중간과 처음이 바뀌는 하노이
'''

def hanoi(num, start, to, finish):
    if num == 1:
        print(start, finish)
    else:
        hanoi(num - 1, start, finish, to)
        print(start, finish)
        hanoi(num - 1, to, start, finish)
    
hanoi(N, 1, 2, 3)