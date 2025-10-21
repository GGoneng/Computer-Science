# 단순 연결 구조 리스트
# - 노드 : 데이터를 저장하는 곳 
# - 링크 : 다른 노드를 가리키는 변수, 하나의 노드에 하나 이상의 링크 존재

class Node:
    def __init__(self, element, link=None):
        self.data = element
        self.link = link

    def append(self, node):
        if node is not None:
            node.link = self.link
            self.link = node

    def popNext(self):
        next = self.link
        if next is not None:
            self.link = next.link
        return next
    
class LinkedList: # Head만 관리하면 됨. 데이터는 Node가 관리, 단점으로 데이터에 접근하기 위하여 getNode를 여러 번 수행해야 함.
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
            ptr = ptr.link
        return ptr

    # getNode 메서드를 통해 찾아낸 노드 주소에서 그 안에 들은 데이터를 반환
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data

    # before (pos-1 번째 Node)를 찾아서 append
    def insert(self, pos, e):
        node = Node(e, None)
        before = self.getNode(pos-1)

        if before == None:
            node.link = self.head
            self.head = node
        
        else:
            before.append(node)

    # before (pos-1 번째 Node)를 찾아서 popNext, Head Node 일 시, 교체
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head
            if self.head is not None:
                self.head = self.head.link
            return before

        else: return before.popNext()

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count
    
    def display(self, msg="LinkedList : "):
        print(msg, end="")
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end=" -> ")
            ptr = ptr.link
        print("None")

if __name__ == "__main__":
    s = LinkedList()
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

