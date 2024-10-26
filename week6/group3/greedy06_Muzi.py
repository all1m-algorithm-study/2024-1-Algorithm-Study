def solution(food_times, k):
    t, p, answer = 0, 0, 0
    #food = {i:food_times[i] for i in range(len(food_times))}
    
    while t < k: # 중단 시간 전 동안 이루어지는 과정           
        # 일단 먹는다
        food_times[p]-=1
        t+=1 
        while True: # 이동한 지점이 0이 아닐 때까지 이동하는 루프
            # 1. 일단 이동한다
            if p != len(food_times)-1:
                p+=1
            else:
                p=0
            # 2. 이동 지점에 음식이 존재하는지 확인한다
            if food_times[p]>0:
                answer = p+1 # 다음 이동 지점인 p를 answer에 대입
                print(answer)
                # 멈추기 (이동 반복문 탈출)
                break
            else:
                continue# 더 이동한다
    return answer
#print(solution([3,1,2],5))
print(solution([3, 1, 1, 2], 6))


