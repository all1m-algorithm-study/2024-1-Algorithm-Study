import sys
input = sys.stdin.readline

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    mine=list(map(int,input().split()))
    # 1. 2차원 리스트로 입력값 정리
    row = [[] for _ in range(m)]

    for i in range(m):  #0,1,2,3/4
        for k in range(n): # 0,1,2/3
            row[i].insert(k,mine[m*k+i])
    #print(row)
    # 2. 테스트케이스마다 계산
    # => 갈 수 있는 다음 열 수 중에서 가장 큰 것만 더하다 보면 최대 값이 나옴 <= 아님!!!!
    # 수정) dp[0]: 갈 수 있는 위치 / dp[0][0]: dp[i], 전 단계에서 가서 얻은 금의 최대 가치/ 값: 갈 수 있는 위치(에 따른 금의 가치)
    # dp[0][0]을 계속 갱신한다  
    key = [-1,0,1]
    dp = [[0]*len(key) for _ in range(n)]
    path = [[] for _ in range(m)]   # 차수마다 길(인덱스) 추적 기존의 dp[0] () m+1 <= Index of Error 방지
    # 0열 초기화
    for i in range(n):
        path[0].append((i,row[0][i]))

    # 시작
    for t in range(m-1): # 차수 (광산 행렬 열)
        #print(t,"차")        # 차수 0열 갱신
        #print('path',path)
        # 차수 별로 dp 행렬 채우기
        for i in range(n):  # dp 행
            for j in range(3):  # dp 열  
                pos = path[t][i][0]+key[j]   # 다음에 가능한 포지션
                if pos<0 or pos>=n:   # 범위 넘어갈 시
                    dp[i][j]=(-1,-1)  # X처리 
                    continue
                value = row[t+1][pos]
                dp[i][j]=(pos,value)
            # 다음 위치 찾기
            # value가 max인 열의 pos값 찾기
            _max = 0
            max_pos = 0
            #print(dp[i]) #행렬 점검용
            for pos, value in dp[i]:
                if(_max < value):
                    _max = value
                    max_pos = pos
            path[t+1].append((max_pos,_max))
            # 다음 행
    #print(path)    # 최종 루트

    sum = [0]*m
    #sum = [[] for _ in range(m)]
    for i in range(n):
        for k in range(m):
            #sum[i].append(path[k][i][1])
            sum[i]+=path[k][i][1]
        print(sum[i])  # 시작 행 별로 얻을 수 있는 최대 가치
    print(max(sum))



"""
    dp[0] = row[0].index(max(row[0]))   # dp[i]=가야할 i번째 열 위치
    key = [-1,0,1]
    for i in range(1,m):
        cur = dp[i-1]
        next = []
        for k in key:
            cur+=k
            if cur>=0 and cur<=2:
                next.append(cur)
            cur-=k
        dp[i] = max(next)
    
    print(dp)
    sum=0
    for i in range(m):
        print(row[i][dp[i]])
        sum+=row[i][dp[i]]
    print(sum)
"""
