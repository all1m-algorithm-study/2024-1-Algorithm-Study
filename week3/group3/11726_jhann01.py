#11726
#2×n 타일링

import sys
input = sys.stdin.readline


n = int(input())
Solution = [0]*1001

#n=1
#1 |

#n=2
#2 ||, =

#n=3
#3 |||, =|, |=

#n=4
#5 ==, =||, ||=, ||||, |=|

#n=5
# ==|, |==, =|=, |||=, =|||, |||||, |=||, ||=|

Solution[1] = 1
Solution[2] = 2

for i in range(3, n+1):
    Solution[i] = (Solution[i-1] + Solution[i-2])%10007
print(Solution[n])




