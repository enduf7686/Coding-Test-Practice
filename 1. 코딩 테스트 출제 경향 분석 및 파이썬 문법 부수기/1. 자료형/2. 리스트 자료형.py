# 리스트 자료형

# 1. 리스트 만들기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 리스트는 대괄호
print(a)

print(a[4])  # 4번 인덱스에 접금

a = list()  # 빈 리스트 선언 방법 1
print(a)

a = []  # 빈 리스트 선언 방법 2
print(a)

n = 10
a = [0] * n  # 길이가 n이고, 모든 값이 0인 리스트 초기화
print(a)

# 2. 리스트의 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[-1])  # 뒤에서 첫 번째 원소 출력

print(a[-3])  # 뒤에서 세 번째 원소 출력

print(a[1:4])  # 1번 부터 3번까지 슬라이싱

# 3. 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]  # 0부터 19까지 홀수만 포함하는 리스트
print(array)

array = [i * i for i in range(1, 10)]  # 1부터 9까지의 제곱 값을 포함하는 리스트
print(array)

n = 3
m = 4
array = [[0] * m for _ in range(n)]  # 3 * 4크기의 이차원 리스트 초기화
print(array)

# 4. 리스트 관련 기타 메소드
a = [1, 3, 4]

a.append(2)  # 리스트에 원소 삽입
print("삽입: ", a)

a.sort()  # 오름차순으로 정렬
print("오름차순 정렬: ", a)

a.sort(reverse=True)
print("내림차순 정렬: ", a)

a.reverse()  # 리스트 원소 뒤집기
print("리스트 뒤집기: ", a)

a.insert(2, 3)  # 특정 인덱스에 원소 추가
print("인덱스 2번에 3추가", a)

print("값이 3인 데이터의 갯수: ", a.count(3))  # 특정 값을 지닌 원소의 갯수 세기

a.remove(1)  # 특정 값을 지닌 원소 삭제
print(a)

# 여러개의 값을 한번에 삭제하는 방법(remove()는 하나만 삭제 가능)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove_set = {3, 5}

result_set = [i for i in a if i not in remove_set]  # 리스트 컴프리헨션을 이용한다.
print(result_set)