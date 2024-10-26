import sys
input = sys.stdin.readline

s = list(input())
s.pop() # 개행문자 날리기 ('/n')
s.sort(reverse=True) 

result = 0

for i in s:
    if result == 0 or int(i) <= 1: # 수정 int(i) == 0
        result += int(i)
    else:
        result *= int(i)

print(result)
