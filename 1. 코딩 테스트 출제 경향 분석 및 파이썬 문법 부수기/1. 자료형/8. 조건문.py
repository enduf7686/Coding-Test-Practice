# 조건문

# 1. 조건문 만들기
score = 85
if score >= 90:
  print("학점 A") # 파이썬에서는 코드 블록을 들여쓰기로 구분한다.
elif score >= 80:
  print("학점 B")
elif score >= 70:
  print("학점 C")
else:
  print("학점 F")

# 2. 논리 연산자
A = True
B = False

print(A and B)
print(A or B)
print(not A)

a = [1, 2, 3, 4]
n = 3
if n in a: # in 연산자
  print("리스트에 포함되어 있습니다.")

data = "Hello World"
c = 'x'
if c not in data: # not in 연산자
  print("문자열에 포함되어 있지 않습니다.")

# 3. 조건부 표현식
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)