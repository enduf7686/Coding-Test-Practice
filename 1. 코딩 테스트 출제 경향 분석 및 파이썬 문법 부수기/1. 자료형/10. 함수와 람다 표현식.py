# 함수와 람다 표현식

# 1. 함수 만들기
def add(a, b):
  return a + b

print(add(3, 4))

def operator(a, b):
  add_var = a + b
  sub_var = a - b
  mul_var = a * b
  div_var = a / b
  return add_var, sub_var, mul_var, div_var # 파이썬에서는 여러 개의 반환 값을 가질 수 있음

a, b, c, d = operator(7, 3)
print(a, b, c, d)

a = 10

def func():
  global a # 함수 내에서 전역 변수에 접근하려면 global 키워드를 이용해야 함
  a += 1

func()
print(a)

# 2. 람다 표현식 만들기
print((lambda a, b: a + b)(3, 7)) # print(add(3, 7))

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
print(sorted(array, key=lambda x: x[1], reverse = True)) # sorted() 함수에서 정렬 기준을 표현할 때 많이 사용된다.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = list(map(lambda a, b: a + b, list1, list2)) # map(): 각각의 원소에 특정한 함수를 적용할 때 사용하는 함수

print(result)

