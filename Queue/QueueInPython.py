# Python 모듈을 통한 자료구조
import queue
import random

q = queue.Queue(8)

print("삽입 순서: ", end="")

while not q.full():
    v = random.randint(0, 100)
    q.put(v)
    print(v, end=" ")
print()

print("삭제 순서: ", end="")

while not q.empty():
    print(q.get(), end=" ")
print()


import collections

dq = collections.deque()

print("Deque is not Empty." if dq else "Deque is Empty.")

for i in range(9):
    if i % 2 == 0: dq.append(i)
    else: dq.appendleft(i)

print("홀수는 전단 짝수는 후단 삽입", dq)

for i in range(2): dq.popleft()
for i in range(3): dq.pop()

print("전단 삭제 2번, 후단 삭제 3번", dq)

for i in range(9, 14): dq.appendleft(i)

print("전단에 9 ~ 13 삽입          ", dq)

print("Deque is not Empty." if dq else "Deque is Empty.")