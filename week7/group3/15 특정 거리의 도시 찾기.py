import sys
from collections import deque

# N,M,K,X = 4,4,1,1 # 도시 수, 도로 수, 목표 최단거리, 출발점
# adj = [[], [2,3],[3,4],[1,2],[2]]

input = sys.stdin.readline
q = deque()

N,M,K,X = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int,input().split())
    adj[A].append(B)
    adj[B].append(A)

def bfs(start):
    visited = [False] * (N+1)
    result = []
    tmp = []
    # 초기화
    dist = 0
    q.append([start,dist])
    visited[start] = True

    while q:
        V = q[0][0]     # 확인하고자 하는 정점의 번호
    
        if dist == K:      # 탈출 조건: 최단거리가 K인 걸 발견해야할 때
            for city in q:    # 큐에 있는 도시 중 최단거리가 K인 걸 모두 결과 리스트에 추가
                if city[1] == K:
                    result.append(city[0])
        
            if result == []:  # 큐가 비었거나 최단거리가 K인 도시가 존재하지 않을 경우
                print(-1)
                break
        
            result.sort()     # 오름차순 정렬        
            for v in result:  # 출력
                print(v)
            break 

        # 최단거리 계산
        for v in adj[V]:
            tmp.append(visited[v])
        if tmp != [True]*(len(adj[V])): # 정점 v의 인접 도시들이 전부 방문하지 않았을 때만 거리+1
            dist+=1
        tmp.clear() # 초기화

        # 방문 안 한 도시들 큐에 최단거리와 함께 집어넣고 방문 처리
        for v in adj[V]:
            if not visited[v]:
                q.append([v,dist])
                visited[v] = True   
        q.popleft()

        if q == deque(): # 큐가 비면 탈출
            print(-1)
            break
bfs(X)