import sys
input = sys.stdin.readline

# 이론적으로 맞는 재귀꼴은 아닌듯 합니다...

def recur(substring):
    #stacked: return 이후 즉시 return 하는게 아니므로 return 값을 저장해놓는 변수로 사용
    #counting: 문자열 길이를 구하기 위해 카운팅
    #pointer: 문자열 인덱스
    stacked, counting, pointer = 0, 0, 0
    
    # 입력값을 문자열 인덱스로 조회
    while pointer < len(substring):
        # ( -> 재귀호출
        if substring[pointer] == '(':
            counting -= 1
            a, b = recur(substring[pointer+1:])
            stacked += int(substring[pointer-1]) * a
            pointer += b+1
        # ) -> 값 반환 __ base case에 해당...
        elif substring[pointer] == ')':
            return stacked + counting, pointer
        # c -> 문자열 길이 카운팅
        else:
            counting += 1
        pointer+=1
    return stacked + counting

string = input().rstrip()
print(recur(string))