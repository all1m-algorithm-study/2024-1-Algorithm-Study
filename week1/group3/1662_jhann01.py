S = input()

stack = []
N = len(S)

for i in range(N - 1, -1, -1):
    stack.append(S[i])
    if i == N - 1:
        continue
    if S[i + 1] == "(":
        s = 0  
        stack.pop()
        stack.pop()
        while stack:
            n = stack.pop()
            if n == ")":
                break
            else:
                if type(n) == str:
                    s += 1
                else:
                    s += n
        stack.append(s * int(S[i]))

ans = 0
while stack:
    n = stack.pop()
    if type(n) == int:
        ans += n
    else:
        ans += 1

print(ans)