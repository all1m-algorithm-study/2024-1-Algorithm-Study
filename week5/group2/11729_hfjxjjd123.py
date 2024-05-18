n = int(input())

def hanoi_move(n, s_point, d_point):
    if n == 1:
        print("{} {}".format(s_point, d_point))
    else:
        via = 6-s_point-d_point
        hanoi_move(n-1, s_point, via)
        print("{} {}".format(s_point, d_point))
        hanoi_move(n-1, via, d_point)

print(2**n-1)
hanoi_move(n, 1, 3)
