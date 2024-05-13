n = int(input())

arr = []
for i in range(n):
    arr.append([" "] * (2*n - 1))

def draw_recur(n, i, j):
    # Base Case
    if n == 3:
        arr[i][j] = "*"
        arr[i+1][j-1] = "*"
        arr[i+1][j+1] = "*"
        arr[i+2][j-2] = "*"
        arr[i+2][j-1] = "*"
        arr[i+2][j] = "*"
        arr[i+2][j+1] = "*"
        arr[i+2][j+2] = "*"
    else:
        n = n//2
        draw_recur(n, i, j)
        draw_recur(n, i+n, j-n)
        draw_recur(n, i+n, j+n)


draw_recur(n, 0, n-1)
for a in arr:
    print("".join(a))