# 시각

# 나의 풀이
N = int(input())

hour, minute, second = 0, 0, 0

check = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]

answer = 0

while hour <= N:
  second += 1
  if second == 60:
    minute += 1
    second = 0
  if minute == 60:
    hour += 1
    minute = 0

  if hour in check:
    answer += 1
    continue
  if minute in check:
    answer += 1
    continue
  if second in check:
    answer += 1
    continue
  
print(answer)

# 예시 답안
h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
  
# 모든 경우가 86,400가지밖에 존재하지 않기 때문에 하나씩 모두 세서 쉽게 풀수 있는 문제
# 완전 탐색 유형으로 분류되기도 함
# 전체 데이터의 갯수가 100만 개 이하라면 완전 탐색을 고려해보자
# 숫자를 문자열 자료형으로 바꿔서 붙힌 후에 확인하는 스킬 유심히 보기