# 왕실의 나이트

# 나의 풀이
location = input()

alp_to_num = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
x, y = alp_to_num[location[0]], int(location[1])

dx = [-1, 1, 2, 2, -1, 1, -2, -2]
dy = [2, 2, -1, 1, -2, -2, -1, 1]

answer = 0

# 예시 답안
for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > 8 or ny > 8:
    continue

  answer += 1

print(answer)

# 예시 답안
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
    result += 1

print(result)

# '상하좌우' 문제에서는 dx, dy 리스트를 선언하여 이동할 방향을 기록할 수 있도록 하였다. 이번 문제에서는 steps 변수가 dx, dy의 기능을 대신하여 수행한다. 2가지 형태 모두 자주 사용되므로, 참고하도록 하자