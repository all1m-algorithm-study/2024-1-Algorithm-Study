n = int(input())
k = int(input())

start, end = 1, k
optimal_val = 0

while start <= end:
    mid = (start + end) // 2
    
    count = 0
    for i in range(1, n+1):
        count += min(mid//i, n)
    
    if count >= k:
        optimal_val = mid
        end = mid - 1
    else:
        start = mid + 1
        
print(optimal_val)