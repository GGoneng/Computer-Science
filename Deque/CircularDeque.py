# Deque (double-ended queue)는 전단, 후단 모두에서 삽입, 삭제 가능한 큐
# 원형 Deque 기준, AddFront, DeleteRear 메서드는 반시계 방향
# AddRear, DeleteFront 메서드는 시계 방향

from ArrayQueue import *

class CircularDeque(ArrayQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)
    
    # ArrayQueue에 정의한 메서드 사용
    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            print("Deque is Full.")
        
    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else:
            print("Deque is Empty.")
    
    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            print("Deque is Empty.")

if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i % 2 == 0: dq.addRear(i)
        else: dq.addFront(i)
    
    dq.display("홀수는 전단 짝수는 후단 삽입")

    for i in range(2): dq.deleteFront()
    for i in range(3): dq.deleteRear()

    for i in range(9, 14): dq.addFront(i)
    dq.display("전단에 9 ~ 13 삽입")

