"""
1. 연속되는지 검사
1.1 연속된다 => 카운트,인덱스 1씩 올리기
1.2 연속x=>글자 수 계산 및 초기화
2. (연속과 상관없이) 문자열 맨 끝에 도달 시
최종 글자수 계산
#문제: 계산은 초기화 전에 해야함
# 계산 시점
1. 연속되지 않으면서 cnt>1
2. 맨 끝 인덱스일 때
=> 연속ㅇ 맨끝 ㅇ /연속x 
"""

#s='aabbaccc'
#s='ababcdcdababcdcd'
#s='abcabcdede'
s='abcabcabcabcdededededede'
#s='xababcdcdababcdcd'
#57.1점
def solution(s):
    # 완전 탐색으로 단위 1부터 1000까지 가능
    length = len(s)
    result = [length]*(length//2)    # 단위별 결과 담는 리스트
    
    for unit in range(1,length//2+1):       # 단위가 절반 이후는 의미가 없음 (같은 패턴이 2개 이상 나올 수 없어서)
        # 초기화
        prior = s[0:0+unit]     # 현재 문자와 비교할 이전 문자열
        cnt=1                   # 특정 패턴 수
        i=unit                  # 위치(인덱스)를 나타내는 변수  
        #print('unit:',unit)
        while i<length:
            #print(prior,i,s[i:i+unit])
            if prior == s[i:i+unit]:
                cnt+=1
                if i+unit == length: 
                    result[unit-1] -= cnt*unit-(1+unit) # 3ab면 ababab->3ab (6->3)
                    #print('끝',cnt)
                i+=unit
                continue
            if cnt > 1:  # cnt=1은 문자열 변화 없음
                result[unit-1] -= cnt*unit-(1+unit)
                #print(cnt)
            prior = s[i:i+unit] # 새 패턴 생성
            cnt=0
    
    #print(result)
    return min(result)

print(solution(s))



# 문제: 인덱스 0일 때 자기자신 당연히 됨 그래서 안 되면 [1]부터 다시 진행해야하는데 i+unit으로 뜀
# 단위가 2이상일 때 시작하고 바로 연속하지 않으면 인덱스 1부터 시작해야하는데 그다음 단위로 루프를 시작함
"""
def solution(s):
    # 완전 탐색으로 단위 1부터 1000까지 가능
    unit = 0    # 단위
    length = len(s)
    result = [length]*(length//2)    # 단위별 결과 담는 리스트
    for u in range(length//2):  # 단위가 절반 이후는 의미가 없음 (같은 패턴이 2개 이상 나올 수 없어서)
        unit += 1
        # 초기화
        prior = s[0:0+unit]     # 현재 문자와 비교할 이전 문자열
        cnt=1                   # 특정 패턴 수
        i=unit                  # 위치(인덱스)를 나타내는 변수  
        print('unit',unit,s)      
        while i<length:
            print(prior,'/',s[i],i)

            # 연속되는지 검사
            if s.find(prior,i) == i:   # 본인부터 패턴 검색해서 바로 자신이 그 패턴의 시작이면
                cnt += 1
                if i+unit == length: 
                    result[u] -= cnt*unit-(1+unit) # 3ab면 ababab->3ab (6->3)
                    print(cnt)
                i+=unit
                continue
            # 연속 X
            if cnt > 1:  # cnt=1은 문자열 변화 없음
                print(cnt)
                result[u] -= cnt*unit-(1+unit)
                print(u+1,':',result[u])
            # init
            cnt=0
            if i==unit:
                prior = s[1:1+unit]
                i=1
            prior = s[i:i+unit] # 새 패턴 생성
            
 
    answer = min(result)
    print(result)
    return answer
"""