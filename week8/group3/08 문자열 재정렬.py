# 0~9: 48~57
# 'A': 65
S = list(input())

sum=0
for i in range(len(S)):
    S[i]=ord(S[i])  # 아스키코드로 변환
    if S[i]<65:
        sum+=int(chr(S[i])) # 변환되었던 숫자 문자를 정수형으로 변환

S.sort()

for i in range(len(S)):
    if S[i]>=65:
        print(chr(S[i]),end='') # 알파벳만 숫자(아스키코드)에서 다시 본래 문자로 변환
print(sum,end='')