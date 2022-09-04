# 자주 사용되는 표준 라이브러리

# 1. 내장 함수
print(sum([1, 2, 3, 4, 5])) # sum(): 리스트와 같은 iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환

print(min(3, 4, 9, 2)) # min(): 파라미터가 2개 이상 들어왔을 때. 가장 작은 값을 반환

print(max(1, 5, 10, 3)) # max(): 파라미터가 2개 이상 들어왔을 때, 가장 큰 값을 반환

print(sorted([1, 4, 5, 2, 3])) # sorted(): iterable 객체가 입력으로 주어졌을 때, 정렬된 결과를 반환

# 2. itertools
from itertools import permutations # 순열(순서 상관 O)
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

from itertools import combinations # 조합(순서 상관 X)
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

from itertools import product # 중복 순열
data = ['A', 'B', 'C']
result = list(product(data, repeat = 2))
print(result)

from itertools import combinations_with_replacement # 중복 조합
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 3))
print(result)

# 3. collections
from collections import Counter # iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려줌
counter = Counter(['red', 'blue', 'green', 'green', 'green', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))

# 4. math
import math
print(math.factorial(5)) # 팩토리얼

print(math.gcd(21, 14)) # 최대 공약수
print(21 * 14 // math.gcd(21, 14)) # 최소 공배수는 따로 구하는 함수가 없으므로 공식을 이용하여 구함