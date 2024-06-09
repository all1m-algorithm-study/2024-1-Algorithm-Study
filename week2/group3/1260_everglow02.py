import sys
input = sys.stdin.readline

from collections import deque 

N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(M): # 그래프 생성
  node1, node2 = map(int,input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

for adj in graph: # 오름차순 정렬5
  adj.sort()

def DFS(graph, visited, start):
  if visited[start]:
    return
  visited[start] = True
  print(start, end=" ")
  for dest in graph[start]:
    DFS(graph, visited, dest)

DFS(graph, visited, V)
visited = [False for _ in range(N+1)]

next = deque()
cur = 0
print("\n", end= "")
def BFS(graph, visited, start):
  next = deque([start])
  visited[start] = True

  while(next): # 큐가 비어있지 않는 경우 (= 인접한 노드가 있을 경우)
    cur = next.popleft() # 현재 보고 있는 노드
    print(cur, end=" ") # 방문순서에 적음
    for i in graph[cur]:    
      if not visited[i]: # 방문 했는지 검사
        visited[i] = True # 방문했다고 기록
        next.append(i) # 기록과 동시에 큐에 집어넣기


BFS(graph, visited, V)