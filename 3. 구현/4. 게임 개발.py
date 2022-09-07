# 게임 개발

# 나의 풀이
N, M = map(int, input().split())
x, y, direction = map(int, input().split())

game_map = [[0] * M for _ in range(N)]
for i in range(N):
    game_map[i] = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 0
check = 0

while True:
    if check == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if nx < 0 or ny < 0 or nx >= M or ny >= N or game_map[ny][nx] == 1:
            break

        x, y = nx, ny
        check = 0

    game_map[y][x] = 2

    direction -= 1
    if direction < 0:
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or ny < 0 or nx >= M or ny >= N or game_map[ny][
            nx] == 1 or game_map[ny][nx] == 2:
        check += 1
        continue

    x, y = nx, ny
    check = 0  # 문제 풀고 난 다음에 발견함. 테스트 케이스는 맞았으나 실제 테스트에서는 틀렸을 듯

for i in range(N):
    answer += game_map[i].count(2)

print(answer)
# 예시 답안
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(N)]
# 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(N):
    array[i] = list(map(int, input().split()))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)

# 왼쪽으로 회전할 때 함수 이용하는 것이 좋을 것 같다.
# 예시 답안에서는 방문한 좌표 리스트 따로 게임 맵 리스트를 따로 놓았다. 나는 한 리스트에서 해결하려고 했다. 어느 것이 더 좋은 풀이일까?
# 한 칸 이동하고 check를 다시 0으로 초기화 해야 하는데 실수했다. 다음부터는 주의하자.
# 2차원 배열에서 원소 접근할 때 실수하지 않기 list[x, y] => X, list[y][x] => O
