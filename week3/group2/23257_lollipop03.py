import sys
input = sys.stdin.readline #input을 빠르게 받아옵니다

'''
bitwise xor은 교환법칙과 결합법칙이 성립 ->
dp에 1,2,4,8,16,32,64개 합쳐놓은거 전부 set에 저장
M을 비트를 체크하고 dp에서 뽑아서 xor하기
'''

N, M = map(int,input().split())
dp = [set(abs(int(x)) for x in input().strip().split())]

dp_max = M.bit_length() #M의 비트 길이를 구한다 ex) 5 -> 101 -> 3
for i in range(1, dp_max): #길이수 만큼 xor 미리 구해놓기
    newset = set()
    for j in dp[i-1]: #이전 걸로 서로 xor 시켜서
        for k in dp[i-1]:
            newset.add(j^k) #bitwise xor
    dp.append(newset) #저장

ansset = set()
for i in range(len(dp)):#미리 구해놓은 dp만큼만 돌리기
    if (M & (1 << i)): # &가 bitwise and이기 때문에,
        # 1을 bitshift 시키면서, 1이 있는 위치를 확인,
        # 1 and 1이 성립하면 1을 반환하기 때문에 True, 아니면 False라 넘어감
        if ansset:
            temp_set = set()
            for j in ansset: #이미 돌린 거에다가 새로 xor할거 합치기
                for k in dp[i]:
                    temp_set.add(j ^ k)
            ansset = temp_set #아무것도 없는 초기조건이라면 넣기
        else:
            ansset = dp[i]
print(max(ansset)) #max값 출력