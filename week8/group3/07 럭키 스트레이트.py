N = input()
length = len(N)

sum1,sum2 = 0,0
for i in range(length):
    if i < length/2:
        sum1 += int(N[i])
    else:
        sum2 += int(N[i])

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')