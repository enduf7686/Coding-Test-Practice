# 꼭 필요한 자료구조 기초

# 스택
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# 스택은 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작한다.

# 큐
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(5)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

# 큐는 collections 모듈에서 deque 자료구조를 활용하자. deque은 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트에 비해 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다.