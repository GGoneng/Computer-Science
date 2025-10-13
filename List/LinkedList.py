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
    
class LinkedList: # Head만 관리하면 됨. 데이터는 Node가 관리
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    # List는 메모리 부족이 아닌 이상 포화 상태가 안되므로 False 반환
    def isFull(self):
        return False