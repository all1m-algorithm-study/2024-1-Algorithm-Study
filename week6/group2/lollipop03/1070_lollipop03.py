import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    tlist = [[] for _ in range(V + 1)]
    for _ in range(E):
        x, y = map(int, input().split())
        tlist[x].append(y)
        tlist[y].append(x)
    
    flist = set()
    slist = set()
    condition = True

    '''
    1부터 넣으면서 둘 다에 없으면 1번에 넣고 BFS
        BFS중 현재를 cur, 반대쪽 opp
        cur 연결 cur에 있으면 NO
        없으면 opp에 넣고 que 넣기
    끝번까지 다 돌고 멀쩡하면 YES
    '''
    
    for i in range(1, V + 1):
        if i not in flist and i not in slist:
            queue = deque([i])
            flist.add(i)
            
            while queue and condition:
                node = queue.popleft()
                if node in flist:
                    curset = flist
                    oppset = slist
                else:
                    curset = slist
                    oppset = flist
                
                for next in tlist[node]:
                    if next in curset:
                        condition = False
                        break
                    if next not in oppset:
                        oppset.add(next)
                        queue.append(next)
        
        if not condition:
            break
    
    if condition:
        print("YES")
    else:
        print("NO")