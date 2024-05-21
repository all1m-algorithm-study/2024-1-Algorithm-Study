from collections import deque

#N : 정점의 개수
#M : 간선의 개수
#V : 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

#어디서 어디로 가는지 입력
for i in range(M):
    a , b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#정렬
for i in graph:
    i.sort()

#DFS(재귀함수 활용)
def dfs(start): # dfs(1) #dfs(2)에 대하여
    vistied[start] = True #vistied[1] = True, #vistied[2] = True
    print(start, end = " ")# "1 "출력 #"2 "출력

    for x in graph[start]:#graph[1]에 대해서 #graph[2]에 대해서
        if vistied[x] == False:#만약 vistied[2, 3, 4]가 False라면
            ##만약 vistied[1, 4]가 False라면
            ## 만약 vistied[1]은 True이기에 pass
            dfs(x)#dfs(2)로 재귀 #그래서 dfs(4)로 재귀


# BFS(queue 활용)
def bfs(start):
    queue = deque([start])
    vistied[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for y in graph[v]:
            if vistied[y] == False:
                vistied[y] = True
                queue.append(y)






#DFS 출력
vistied = [False] * (N + 1)
dfs(V)
print()

#BFS 출력
vistied = [False] * (N + 1)
bfs(V)








