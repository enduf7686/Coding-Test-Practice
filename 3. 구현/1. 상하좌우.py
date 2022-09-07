# 상하좌우

# 나의 풀이
N = int(input())
directions = input().split()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = [1, 1]

for direction in directions:
  if direction == 'R':
    answer[0] += dy[0]
    answer[1] += dx[0]
  elif direction == 'L':
    answer[0] += dy[1]
    answer[1] += dx[1]
  elif direction == 'D':
    answer[0] += dy[2]
    answer[1] += dx[2]
  else:
    answer[0] += dy[3]
    answer[1] += dx[3]
  if answer[0] == 0:
    answer[0] = 1
  if answer[1] == 0:
    answer[1] = 1
  
print(answer[0], answer[1])

# 예시 답안
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
  
# dx, dy 깔끔하게 쓰는 스킬
# 이동할 좌표 구하기와 이동을 분리하기
# x,y를 리스트에 담을 필요 없었다.

# int 자료형 데이터의 개수에 따른 메모리 사용량
# 1,000개 -> 4KB
# 1,000,000개 -> 4MB
# 10,000,000개 -> 40MB

# 파이썬은 1초에 2000만 번의 연산을 수행한다고 가정한 후 문제를 풀 것