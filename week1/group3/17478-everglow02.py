from sys import stdin
input = stdin.readline

#17478번-재귀함수가 뭔가요?

N = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

question = "\"재귀함수가 뭔가요?\"\n"
str1 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n" 
str2 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n" 
str3 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""

answer = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
returnStr = "라고 답변하였지.\n"

#response(i,N) = iter+returnStr
def response(i,N):
  iter = '_'*4*i
  repetiton = [iter+question,iter+str1,iter+str2,iter+str3]
  lastStr = [iter+question,iter+answer]  
  if (i == N):
    print(''.join(lastStr))
    return (iter+returnStr)
  else:
    print(''.join(repetiton))
    return response(i+1,N)+(iter+returnStr)
  
print(response(0,N))
