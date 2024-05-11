# Subproblem

큰 원판이 작은 원판 위로 못온다  
= 가장 큰 원판을 제일 먼저 도착지로 옮겨야 한다  
= 가장 큰 원판을 옮기려면 그 위의 `작은 원판들을 모두 빼`야 옮길 수 있다  
= 가장 큰 원판을 도착지로 옮기고, 작은 원판들을 `그대로 큰 원판 위로` 옮기면 된다.  
⇒ `작은 원판들을 모두 빼` = `그대로 큰 원판 위로` : 동일한 연산  
⇒ Hanoi(n) = Hanoi(n-1) → 큰 원판 옮긺 → Hanoi(n-1)

# 점화식

### Hanoi(n, s, d) = Hanoi(n-1, s, tmp) + Move(s, d) + Hanoi(n-1, tmp, d)

# 풀이

## #1 움직임 횟수

A(n) = A(n-1)*2 + 1  
A(1) = 1

## #2 움직임 출력

base case: n=1 → 출력  
중간 Move(s,d) → 출력

```python
*def hanoi_move(n, s_point, d_point):
    if n == 1:
        print("{} {}".format(s_point, d_point))
    else:
        via = 6-s_point-d_point
        hanoi_move(n-1, s_point, via)
        print("{} {}".format(s_point, d_point))
        hanoi_move(n-1, via, d_point)*
```