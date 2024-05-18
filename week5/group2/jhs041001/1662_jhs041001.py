def count(str):
    cnt = 0
    parenthesis_cnt = 0
    start = 0

    for idx in range(len(str)):
        if str[idx] == '(':
            if parenthesis_cnt == 0:
                start = idx
            parenthesis_cnt +=1

        elif str[idx] == ')':
            parenthesis_cnt -=1
            if parenthesis_cnt == 0:
                cnt -=1
                cnt += int(str[start-1]) * count(str[start+1:idx])
                
        else:
            if parenthesis_cnt == 0:
                cnt +=1
    
    return cnt

compressed = input()
print(count(compressed))

