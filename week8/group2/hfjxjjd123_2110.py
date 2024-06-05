import sys
input = sys.stdin.readline

N, C = map(int, input().split())
homes = []
for i in range(N):
    homes.append(int(input()))
homes.sort()

home_criteria = homes[0]
for i in range(len(homes)):
    homes[i] -= home_criteria

start = 0
end = homes[N-1]
mid = length = (start + end)//2
max_len = 0

while start<=end:
    mid = (start+end)//2
    count = 1
    before = 0
    for home in homes:
        if home >= before + mid:
            count += 1
            before = home
    if count >= C:
        max_len = max(max_len, mid)
        start = mid + 1
    else:
        end = mid - 1

print(max_len)