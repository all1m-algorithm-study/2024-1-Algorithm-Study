# ## 33(562(71(9)))

# from sys import stdin
# input = stdin.readline

# def printUnzippedString(priorLeft):  #재귀함수
#     unzippedLength = int(S[priorLeft-1]) * sLen[-1] # K*Q 자리수 
#     left = S.rfind('(', 0, priorLeft)
#     if left == -1:
#         leftOver = S[0:priorLeft-1]
#         sLen.append(unzippedLength + len(leftOver))
#         return  
#     else:
#         right = S.find(')', left)
#         start = right if right < priorLeft else left
#         sLen.append(unzippedLength + len(S[start+1:priorLeft-1]))
#         return printUnzippedString(left)

# # 0.입력 받기
# S = input()
# sLen = []

# left = S.rfind('(')  # leftBracketIdx
# right = S.find(')', left)  # rightBracketIdx
# if left == -1:  # 압축이 없으면
#     print(len(S))
# else:
#     sLen.append(len(S[left+1:right]))
#     printUnzippedString(left)
#     print(sLen[-1])

def rec(tmp, stack):
    while stack:
        top = stack.pop()
        if top == ')':
            tmp += rec(0, stack)
        elif top == '(':
            r = int(stack.pop())
            tmp = tmp * r
            return tmp
        else:
            tmp += 1
    return tmp

str = input()
stack = list(str)
answer = rec(0, stack)
print(answer)