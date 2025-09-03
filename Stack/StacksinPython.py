import queue

# 파이썬에서의 스택 사용법

# 리스트를 사용한 방법
stack_list = []

msg = input("문자열 입력 : ")

for ch in msg:
    stack_list.append(ch)

print("문자열 출력 : ", end="")

while len(stack_list) > 0:
    print(stack_list.pop(), end="")

print()


# queue 모듈을 사용한 방법
stack = queue.LifoQueue(maxsize=100)

msg = input("문자열 입력 : ")

for ch in msg:
    stack.put(ch)

print("문자열 출력 : ", end="")

while not stack.empty():
    print(stack.get(), end="")