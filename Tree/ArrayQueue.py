# Queue는 선입선출(FIFO) 방식으로 데이터를 관리
# 큐에는 Front, Rear가 존재
# Front : 첫 번째 요소 바로 이전의 위치
# Rear : 맨 마지막 요소의 위치


# 큐의 종류는 선형 큐와 원형 큐
# 선형 큐 : 용량을 최대치를 넘기면 자료를 빈 곳으로 밀고 다시 삽입 (비효율적)
# 원형 큐 : 큐를 원형 모양으로 연결 -> 용량의 최대치를 넘기더라도 다시 0부터 자료 삽입

# 큐 클래스 정의
class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    # 큐가 비어 있는지 확인
    def isEmpty(self): return self.front == self.rear
    # 큐가 가득 차있는지 확인 (용량이 5인 큐의 인덱스 : 0 ~ 4, 0부터 4까지 가득 차있다면, 0 == (4 + 1) % 5)
    def isFull(self): return self.front == (self.rear + 1) % self.capacity

    # Enqueue는 Rear에 데이터를 추가하는 메서드
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            print("Queue is Full.")

    # 링 버퍼 : 오래된 자료를 버리고 새로운 자료 삽입 (오버플로우 발생 X)
    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity
    
    # Dequeue는 Front 바로 앞 요소를 추출하는 메서드
    def dequeue(self):
        if not self.isEmpty():
            item = self.array[(self.front + 1) % self.capacity]
            self.array[(self.front + 1) % self.capacity] = None
            self.front = (self.front + 1) % self.capacity
            return item
        else:
            print("Queue is Full.")
    
    # Front 바로 앞 요소를 추출하는 것이 아닌 출력
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            print("Queue is Empty.")

    # Queue 내부 요소의 사이즈  (front : 0, rear : 4, size : 4, capacity : 5 -> (4 - 0 + 5) % 5 = 4)
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    # Queue에 저장된 요소들을 저장된 순서대로 출력
    def display(self, msg):
        print(msg, end="= [")
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity], end=" ")
        print("]")

if __name__ == "__main__":
    import random

    queue = ArrayQueue(10)

    queue.display("초기 상태")

    while not queue.isFull():
        queue.enqueue(random.randint(0, 100))
    
    queue.display("포화 상태")

    print("삭제 순서 : ", end="")
    while not queue.isEmpty():
        print(queue.dequeue(), end=" ")
    print()