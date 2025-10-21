# 이중 연결 구조 리스트
# prev : 이전 노드, next : 단순 연결 구조의 link와 같음 (다음 노드)

class DNode:
    def __init__(self, element, prev=None, next=None):
        self.data = element
        self.next = next
        self.prev = prev
    
    # append: 노드의 뒤에 노드 추가
    # 새롭게 추가될 노드의 next는 self의 next => 중간에 넣는게 아니라면 항상 None
    # 새롭게 추가될 노드의 prev는 self 본인 => self 본인 뒤에 append를 시켜야하므로 self
    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self

            # 새롭게 append한 Node가 중간에 들어갔다면, 새로운 Node의 next의 prev는 새로운 Node
            if node.next is not None:
                node.next.prev = node
            self.next = node

    # next 요소를 pop    
    def popNext(self):
        # node 변수를 self.next로 주고 self.next는 node 다음 요소, node 다음 요소의 prev는 self
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node

class DblLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # List는 메모리 부족이 아닌 이상 포화 상태가 안되므로 False 반환
    def isFull(self):
        return False
    
    # pos번째 노드의 요소를 return 하기 위하여, ptr이 pos번 link를 따라가면 해당 노드를 찾을 수 있음
    def getNode(self, pos):
        if pos < 0 : return None
        ptr = self.head

        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.next
        return ptr

    # getNode 메서드를 통해 찾아낸 노드 주소에서 그 안에 들은 데이터를 반환
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.next
            count += 1
        return count
    

    def display(self, msg="DblLinkedList : "):
        print(msg, end="")
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end=" <=> ")
            ptr = ptr.next
        print("None")

    def insert(self, pos, e):
        node = DNode(e)
        before = self.getNode(pos-1)
        if before == None:
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self.head = node
        else: before.append(node)
    
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return before
        else: before.popNext()

if __name__ == "__main__":
    s = DblLinkedList()
    s.display("연결 리스트 ( 초기 ) : ")
    s.insert(0, 10)
    s.insert(0, 20)
    s.insert(1, 30)
    s.insert(s.size(), 40)
    s.insert(2, 50)
    s.display("연결 리스트 (삽입 X 5) : ")
    s.delete(2)
    s.delete(3)
    s.delete(0)
    s.display("연결 리스트(삭제 X 3) : ")
