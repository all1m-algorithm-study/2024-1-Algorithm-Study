import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001
visited = [0] * MAX #[0 for i in range(MAX)]

# BFS > DFS인 이유: 
# 하나의 노드가 얼마나 깊이까지 가는지 모두 확인해서 최단시간 찾는 건 모든 경로 탐색이므로 비효율적
# 동일 시간(깊이) 내에서 가장 먼저 도착하는 경우 <= 최적 시간

def bfs(p):
    q = deque([p])
    while q:
        p = q.popleft()
        if p == K:
            return visited[p]           # 노드 깊이 = 해당 위치까지 걸린 시간
        for next in (p-1, p+1, 2*p):    # 1초 후 이동 가능한 위치들 
            if 0 <= next < MAX and not visited[next]: # 다음 위치가 범위 내고 방문 전이면
                visited[next] = visited[p] + 1        # 1초 추가  
                q.append(next)

print(bfs(N))