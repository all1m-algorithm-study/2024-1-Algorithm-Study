# 백준 1662 압축
str_stack=[]
input = list(input())
g_stack=[]

def original_str(data):
    num=0
    str_num = 0
    for i in range(0, len(data)):
        if (data[i] =='('):
            str_stack.append('-1')
            g_stack.append('-1')
        elif(data[i] == ')'):
            g_stack.pop()
            a=-2
            while(a != '-1'):
                a = str_stack.pop()
                if (type(a) == int ):
                    num += a
                else:
                    num += 1
            num -= 1
            num *= int(str_stack.pop())
            #for i in range(0, num):
            #    str_stack.append('-3')
            str_stack.append(num)
            num = 0        
            #print(str_stack)
            #print("str_num:", len(str_stack))
        else:
            str_stack.append(data[i])
    #print(str_stack)
    while(str_stack):
        b= str_stack.pop()
        if (type(b) == int):
            str_num += b
        else:
            str_num += 1
    #print(str_num)
    return str_num
        
result= original_str(input)
print(result)