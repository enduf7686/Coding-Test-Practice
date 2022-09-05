# 1이 될 때까지

# 나의 풀이
N, K = map(int, input().split())
count = 0

while True:
    if N == 1:
        break

    if N % K == 0:
        N /= K
        count += 1
    else:
        N -= 1
        count += 1

print(count)

# 예시 답안
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
