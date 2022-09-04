# 자료형

# 1. 정수형
a = 100
print(a)

a = -1
print(a)

# 2. 실수형
a = 157.24
print(a)

a = -64.92
print(a)

a = 5.  # 소수부가 0일 때 0 생략 가능
print(a)

a = -.75  # 정수부가 0일 때 0 생략 가능
print(a)

a = 1e9  # 1000000000
print(a)

a = 75.25e1  # 752.5
print(a)

a = 3954e-3  # 3.954
print(a)

a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:  # 실수 비교 시에는 round() 함수를 이용하여 반올림 해야한다.
    print(True)
else:
    print(False)

# 3. 수 자료형의 연산
a = 7
b = 3

print(a / b)  # 나누기

print(a % b)  # 나머지

print(a // b)  # 몫

print(a**b)  # 거듭제곱
