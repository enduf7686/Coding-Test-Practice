# 숫자 카드 게임

# 나의 풀이
N, M = map(int, input().split())
data = [[0] * M for _ in range(N)]

for i in range(N):
    data[i] = list(map(int, input().split()))

min_array = []

for i in range(N):
    min_array.append(min(data[i]))

print(max(min_array))

# 예시 답안
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

# 이 문제에서는 2차원 배열의 입력을 어떻게 받을 것인지에 대해서 잘 봐야할 것 같다.
