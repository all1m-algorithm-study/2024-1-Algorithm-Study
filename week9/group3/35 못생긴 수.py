# 35 못생긴 수
# 2,3,5만을 약수로 갖는 합성수
# 1,2,3,4,5,6,8,9,10,12,15 ...
# n번째 못생긴 수 찾기

#1 1*2 1*3 2*2 1*5 2*3 4*2 3*3 2*5
#[0] [0]*2 [0]*3 [1]*2 [0]*5 [1]*3 [3]*2 [2]*3 [1]*5

n = int(input())
ugly = [1] #1~1000
key = [2,3,5]
#cnt=0
i=0
while(len(ugly)<1000):
    for u in key:
        result =ugly[i]*u
        if ugly.count(result)==0: # 없을 때만 추가
            #cnt+=1
            ugly.append(result)
    i+=1
ugly.sort()
print(ugly[n-1])
#print(ugly)
#print(cnt,len(ugly),)