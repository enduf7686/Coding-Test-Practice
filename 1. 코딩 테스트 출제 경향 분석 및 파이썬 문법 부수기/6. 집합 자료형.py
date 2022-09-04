# 집합 자료형 (중복 허용 X, 순서가 없음)

# 1. 집합 자료형 만들기
data = set([1, 1, 2, 3, 4, 4, 5]) # 리스트와 문자열을 이용하여 초기화 가능
print(data)

data = {1, 1, 2, 3, 4, 4, 5} # 중괄호와 콤마를 이용하여 초기화 가능
print(data)

# 2. 집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# 3. 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)

data.add(4) # 새로운 원소 추가
print(data)

data.update([5,6]) # 새로운 원소 여러개 추가
print(data)

data.remove(3) # 특정 원소 삭제
print(data)