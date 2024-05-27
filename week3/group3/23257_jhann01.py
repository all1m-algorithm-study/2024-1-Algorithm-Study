#23257
#비트코인은 신이고 나는 무적이다

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
this_month = []

for item in arr:
    this_month.append(abs(item))

month = set(this_month)

for _ in range(m-1):
    month = set(i^j for i in this_month for j in month)

print(max(month))