# 사전 자료형

# 1. 사전 자료형 만들기
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

data = {
  '사과':'Apple',
  '바나나':'Banana',
  '코코넛':'Coconut'
} # 중괄호와 콜론으로 초기화 가능
print(data)

# 2. 사전 자료형 관련 함수
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

key_list = data.keys() # key 데이터만 담은 리스트
value_list = data.values() # value 데이터만 담은 리스트
print(list(key_list)) # 실제 사용 시에는 list()로 형변환을 해줘야 한다.
print(list(value_list))

for key in key_list:
  print(data[key]) # key를 인덱스처럼 활용할 수 있다.