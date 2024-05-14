def move(src,dst,size,reserved):
    if size == 1:
        print(src, dst)
    else:
        move(src, reserved, size-1, dst)
        move(src, dst, 1, reserved)
        move(reserved,dst,size-1, src)

    return

N  = int(input())

turn = 1
for i in range(N-1):
    turn = 2*turn+1

print(turn)
move('1','3',N, '2')

