def cal(num, N, T, arr):
    dp = arr[:]
    if num == 0:
        return False
    for i in range(N):
        if i < num:
            if dp[i] >= T:
                dp[i] = arr[i] + 1
            else:
                dp[i] = T + 1
        else:
            if dp[i - num] > arr[i]:
                return False
            if dp[i - num] + T <= arr[i] + 1:
                dp[i] = arr[i] + 1
            else:
                dp[i] = dp[i - num] + T
    return True

def bst(N, T, arr):
    head = 1
    tail = 200000
    mid = (head + tail) // 2
    while head < tail:
        if cal(mid, N, T, arr):
            tail = mid - 1
        else:
            head = mid + 1
        mid = (head + tail) // 2
    if not cal(mid, N, T, arr):
        mid += 1
    return mid

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    T = int(data[1])
    arr = list(map(int, data[2:2+N]))
    
    arr.sort()
    print(bst(N, T, arr))

if __name__ == "__main__":
    main()
