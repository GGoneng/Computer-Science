# Stack은 후입선출(LIFO) 방식으로 데이터 관리
# 하나의 통로가 입구와 출구 역할을 함

# 스택 클래스 정의
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    # 스택이 비어 있는지 확인
    def isEmpty(self): return self.top == -1
    # 스택이 가득 차있는지 확인
    def isFull(self): return self.top == self.capacity - 1

    # Stack의 Push는 요소를 Stack 안으로 넣는 역할 
    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        # 스택이 가득 찼을때 Push함수를 실행하면 Overflow
        else: 
            print("Stack is Full.") 
    
    # Stack의 Pop은 Stack의 제일 상단에 위치한 요소 (= 마지막에 push한 요소) 추출    
    def pop(self):
        if not self.isEmpty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            return item
        # 스택이 비었는데 Pop함수를 실행하면 Underflow
        else:
            print("Stack is Empty.")
    
    # Pop과 다르게 제일 상단에 위치한 요소를 추출하는 것이 아닌 반환
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("Stack is Empty.")

    def size(self): return self.top + 1


if __name__ == "__main__":

    # 문자열 역순 출력
    stack = ArrayStack(100)

    msg = input("문자열 입력 : ")

    for ch in msg:
        stack.push(ch)

    print(f"문자열 크기 : {stack.size()}")
    print(f"스택 상단에 저장된 문자열 : {stack.peek()}")

    print("문자열 출력 : ", end = "")

    while not stack.isEmpty():
        print(stack.pop(), end = "")

