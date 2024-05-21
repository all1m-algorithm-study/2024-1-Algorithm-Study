#촌수계산
import sys
from collections import deque
input = sys.stdin.readline


#1 : 전체 사람의 수,
n = int(input())

#2 : 서로 다른 두 사람의 번호
p , q = map(int, input().split())

#3 : 부모 자식들 간의 관계의 수
m = int(input())
#4 : 부모 자식간의 관계를 나타내는 두 번호
#앞x : 부모번호     #뒤y : 자식
family = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)

for i in family:
    i.sort()
count = 0


def BFS(start):
    global count
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for y in family[v]:
            if visited[y] == 0:
                visited[y] = 1 + visited[v]
                queue.append(y)
        if v == q:
            print(visited[v] - 1)
            exit()
    if v != q:
        print(-1)
        exit()


BFS(p)
