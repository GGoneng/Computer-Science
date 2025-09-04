from ArrayQueue import *

queue = ArrayQueue(8)

queue.display("초기 상태")
for i in range(6):
    queue.enqueue2(i)

queue.display("삽입 0-5")

queue.enqueue2(6); queue.enqueue2(7)
queue.display("삽입 6, 7")

queue.enqueue2(8); queue.enqueue2(9)
queue.display("삽입 8, 9")

queue.dequeue(); queue.dequeue()
queue.display("삭제 x 2")