str=input()
stack=[]
ans=0
cnt=0

for char in str:
    if char == "(":
        stack.append([k,ans-1])
        ans=0
    elif char == ")":
        print(stack)
        k, r = stack.pop()
        ans=int(k)*ans+r
        
    else:
        k= char
        ans+=1

 
print(ans)




