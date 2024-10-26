def solution(p):
    def dfs(x,s,cntL,cntR):   # [2단계] "균형잡힌 괄호 문자열" u의 인덱스 추출
        checked[x] = True
        if s[x] == '(':
            cntL+=1
        if s[x] == ')':
            cntR+=1
    
        if (cntL or cntR) != 0 and cntL == cntR:
            return x    #return u[0:x+1]

        for i in range(x,len(s)):
            if not checked[i]:
                return dfs(i,s,cntL,cntR)
    # solution 기능 1: bfs로 문자열에서 u,v 분리
    if p == '':
        return p
    checked = [False] * len(p)
    # u, v 분리
    x = dfs(0,p,0,0)
    u = p[0:x+1]
    v = p[x+1:]
    
    # solution 기능 2: u가 "올바른 괄호 문자열"인지 아닌지에 따라 문자열 처리 
    if u == "올바른 괄호 문자열" : 
        # v(나머지)에 대해 수행해서 u,v 분리
        return u + solution(v)
        # x = dfs(0,v,0,0)
        # u = v[0:x+1]
        # v = v[x+1:]       
    else:
        # 다시 재귀적으로 수행한 문자열 v + u로 만든 새 문자열 반환
        # x = dfs(0,v,0,0)
        # v = v[0:x+1]
        u_ = u[1:-1]
        table = u_.maketrans('()', ')(') #new_u = u.replace('(',')').replace(')','(')
        new_u = u_.translate(table)
        return '('+solution(v)+')'+new_u

# (()())()
# )(
# ()))((()
