def recursive(str):
    cnt = 0
    i = 0
    while i < len(str):
        if (ord(str[i]) >= 48 and ord(str[i]) <= 57):
            cnt += 1

        elif(str[i] == ')'):
            return cnt, i+1

        elif(str[i] == '('):
            cnt -= 1
            factor = int(str[i-1])
            res, end = recursive(str[i+1:])
            cnt = cnt + factor * res
            i = i + end
            
        i += 1
    
    return cnt, i+1

s = input()
print(recursive(s)[0])