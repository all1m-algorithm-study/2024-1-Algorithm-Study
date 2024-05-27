import sys
input = sys.stdin.readline

N = int(input())
N //= 3
k = 0 
while N > 1: #비트 연산자로 k 구하기
    k+=1
    N = N >> 1
'''
기본 블럭 = 지금 블럭
k-1동안 반복해서 답 구하기
    블록 밑에다 두번 복사
    원래 줄들 앞뒤로 공백 넣어서 가운데 정렬 맞추기
'''

block = ['  *  ',
         ' * * ',
         '*****']
ans = block[:]
for i in range(k):
    for j in range(len(ans)):
        ans.append(ans[j] + ' '+ ans[j])
        
    for j in range(len(ans)//2):
        ans[j] = ' '*(3*2**i) + ans[j] + ' '*(3*2**i)
print('\n'.join(ans))