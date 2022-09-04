# 입출력

# 1. 전형적인 입력방식
n = int(input()) # 데이터의 개수 입력
data = list(map(int, input().split())) # 각 데이터를 공백으로 구분하여 리스트에 저장 (데이터 수가 많을 때)
print(data)

n, m, k = map(int, input().split()) # 각 데이터를 공백으로 구분하여 n, m, k에 저장 (데이터 수가 적을 때)
print(n, m, k)

# 2. 더 빠르게 입력받기
import sys

data = sys.stdin.readline().rstrip()
print(data)

# 3. 출력
a = 1
b = 2
print(a, b) # 띄어쓰기로 구분되어 출력

answer = 7
print("정답은 " + str(answer) + "입니다.") # 문자열 자료형 끼리만 더하기 연산이 가능하기 때문에 str()로 형변환

answer = 7
print(f"정답은 {answer}입니다.") # f-string: 자료형의 변환 없이 문자열과 정수를 같이 넣을 수 있다.