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