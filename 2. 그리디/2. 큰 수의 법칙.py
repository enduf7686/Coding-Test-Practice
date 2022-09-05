# 큰 수의 법칙

# 나의 풀이
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

answer = 0
count = 0

for _ in range(M):
    if count == K:
        answer += data[1]
        count = 0
    else:
        answer += data[0]
        count += 1

print(answer)

# 예시 답안
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 입력받은 수들 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # M이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:  # M이 0이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)  # 최종 답안 출력

# list()와 map()을 이용하여 여러 데이터를 한꺼번에 입력받을 경우가 많으므로 익숙해져야 한다.
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
