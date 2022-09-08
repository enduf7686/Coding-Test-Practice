# 재귀 함수

# 재귀 함수의 종료 조건(종료 조건을 명시하지 않으면 함수가 무한 호출될 수 있다.)
def recursive_function(i):
  # 100번째 출력했을 때 종료되도록 종료 조건 명시
  if i == 100:
    return
  print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
  recursive_function(i + 1)
  print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

# 재귀적으로 구현한 n!
def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n - 1)

print(factorial_recursive(5))