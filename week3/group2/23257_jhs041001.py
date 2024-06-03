import sys
sys.setrecursionlimit(10000)

N,M   = map(int,input().split())

data = list(map(abs,map(int,input().split())))

prev_state = set(data)

for i in range(M-1):
    temp = set()
    for x in prev_state:
        for y in data:
            temp.add(x ^ y)

    prev_state = temp

print(max(prev_state))