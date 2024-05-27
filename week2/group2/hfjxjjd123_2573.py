import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
mat = []
adj = dict()
glaciers = [0]

for _ in range(N):
    mat.append(list(map(int, input().split())))

vid = 1
for i in range(N):
    for j in range(M):
        if mat[i][j] != 0:
            adj[vid] = []
            glaciers.append(mat[i][j])
            mat[i][j] = vid
            
            if i>0 and mat[i-1][j] != 0:
                adj[vid].append(mat[i-1][j])
                adj[mat[i-1][j]].append(vid)
            if j>0 and mat[i][j-1] != 0:
                adj[vid].append(vid-1)
                adj[vid-1].append(vid)
            
            vid += 1 

num_of_v = vid-1

def melt_out(v):
    global num_of_v
    for a in adj[v]:
        adj[a].remove(v)
    del adj[v]
    num_of_v -= 1
    
def dfs(v):
    is_visited[v] = True
    global counter
    counter += 1
    
    var = 4 - len(adj[v])
    
    for a in adj[v]:
        if is_visited[a] == False:
            dfs(a)
    glaciers[v] -= var

def garbage():
    for i in range(len(is_visited)):
        if is_visited[i] == True:
            if glaciers[i] <= 0:
                melt_out(i)
    

def epoch():
    if len(adj) != 0:
        s =next(iter(adj))
        dfs(s)
        garbage()
    else:
        return False
    return True

cnt = 0
no_sol = False
while True:
    counter = 0
    need_to_visit = num_of_v
    is_visited = [False] * (vid)
    if epoch() == False:
        no_sol = True
        break
    if counter < need_to_visit:
        break
    cnt += 1
if no_sol:
    print(0)
else:
    print(cnt)