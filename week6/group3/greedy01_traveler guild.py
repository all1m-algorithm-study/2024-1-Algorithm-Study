import sys
input = sys.stdin.readline

# 십만 1 1 1 그룹 수 다 보내야하는 걸로 착각
N = int(input())
guild = list(map(int,input().split()))

# 그룹의 인원 수 = 해당 그룹원 중 가장 높은 공포도
# 가장 공포도가 높은 사람 순서대로 
# 그룹의 최댓값을 구하려면 그룹이 잘게 쪼게져야한다는 뜻
# 가장 큰 애의 수만큼 안에 포함되어있어야
guild.sort(reverse=True) # 2 2 2 2 1
cnt = 0

while len(guild) != 0:
    # 빨리 끝낼 수 있는 조건
    if guild[0] == len(guild): 
        cnt += 1 
        guild.clear() # 반복문 탈출
    # 기본 로직
    elif guild[0] <= len(guild): # if면 바로 윗줄에서 반복문 탈출 못함
        for i in range(guild[0]-1): # 최댓값만큼 가장 작은 애부터 조원 뽑기
            guild.pop()
        guild.remove(guild[0])  # 대장도 삭제
        cnt += 1
print(cnt)

#### 아래부터 순차적으로
N = int(input())
guild = list(map(int, input().split()))

guild.sort()

cnt = 0  # 그룹의 수
group_size = 0  # 현재 그룹에 포함된 모험가의 수

for fear in guild:
    group_size += 1  # 현재 그룹에 모험가 추가
    if group_size >= fear:
        cnt += 1  # 그룹 결성
        group_size = 0  # 새로운 그룹 시작

print(cnt)
