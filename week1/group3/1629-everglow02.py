#1629번-곱셈

from sys import stdin
input = stdin.readline

val, exp, mod = map(int,input().split())

def power(val, exp, mod): # val의 exp제곱 (result)을 mod로 나눈 나머지
  if (exp == 0):
    result = 1 
    return result % mod
  elif (exp%2 == 0):
    result = power(val,exp/2,mod)**2
    return result % mod
  elif (exp%2 == 1):
    result = (power(val,int(exp/2),mod)**2) %mod *val
    return result % mod

print(power(val, exp, mod))