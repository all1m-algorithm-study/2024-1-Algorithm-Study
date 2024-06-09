n = int(input())
dad, son = map(int, input().split())
m = int(input())

family = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    parent, child = map(int, input().split())
    family[parent].append(child)
    family[child].append(parent)

for i in range(len(family)-1):
    family[i].sort()
print(family)

count = 0
found = False

def dfs(person, son):
    global count
    global found
    if visited[person]:
        return
    visited[person] = True # if not visited[person]:
    count += 1
    for human in family[person]:
        if human == son:
            print('count', count)
            found = True
            exit()
        else: 
            dfs(human,son) 
  
dfs(dad,son)
if not found:
    print(-1)