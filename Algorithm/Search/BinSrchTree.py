# 이진 탐색 트리를 위한 이진 트리
class BSTNode:
    def __init__(self, key, value):
        self.key = key 
        self.value = value # Value 값 추가
        self.left = None
        self.right = None

# 이진 탐색 트리의 탐색 연산
def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

# 이진 탐색 트리의 탐색 연산 (Value 값 비교, 전위순회)   
def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)

    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)

# 이진 탐색 트리의 삽입 연산
def insert_bst(root, node):
    if root == None: # root가 공백이라면, 이 위치에 삽입
        return node
    
    if node.key == root.key: # root와 node의 key 값이 같다면, 중복 key 값을 방지하기 위하여 삽입 X
        return root

    # node의 key 값이 root의 key 값 보다 작을 시 root의 left에 삽입 연산을 순환 호출    
    if node.key < root.key:
        root.left = insert_bst(root.left, node)

    # node의 key 값이 root의 key 값 보다 클 시 root의 right에 삽입 연산을 순환 호출        
    else:
        root.right = insert_bst(root.right, node)

    return root
    
# 이진 탐색 트리의 삭제 연산
def delete_bst(root, key):
    if root == None:
        return root

    # key 탐색
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    
    # key가 루트의 키와 같으면 root를 삭제
    else:
        # Case 1 : 단말 노드 or Case 2 : 오른쪽 자식만 있는 경우
        if root.left == None:
            return root.right
        
        # Case 2 : 왼쪽 자식만 있는 경우
        if root.right == None:
            return root.left
        
        # Case 3 : 두 자식이 모두 있는 경우
        # 후계자 찾기 (오른쪽 서브트리 최소 노드)
        succ = root.right

        # 최소 노드 찾기
        while succ.left != None:
            succ = succ.left

        # root의 key와 value를 후계자 것으로 변경
        root.key = succ.key
        root.value = succ.value

        # 후계자 남은 데이터 제거
        root.right = delete_bst(root.right, succ.key)
    
    return root

def preorder(n):
    if n is not None:
        print(n.value, end=" ")
        preorder(n.left)
        preorder(n.right)

def print_node(msg, n):
    print(msg, n.value if n != None else "탐색 실패")

def print_tree(msg, r):
    print(msg, end = "")
    preorder(r)
    print()

if __name__ == "__main__":
    data = [(6, "여섯"), (8, "여덟"), (2, "둘"), (4, "넷"), (7, "일곱"),
            (5, "다섯"), (1, "하나"), (9, "아홉"), (3, "셋"), (0, "영")]
    
    root = None
    for i in range(0, len(data)):
        root = insert_bst(root, BSTNode(data[i][0], data[i][1]))
    
    print_tree("최초 : ", root)

    n = search_bst(root, 3);   print_node("srch 3 : ", n)
    n = search_bst(root, 8);   print_node("srch 8 : ", n)
    n = search_bst(root, 0);   print_node("srch 0 : ", n)
    n = search_bst(root, 10);  print_node("srch 10 : ", n)

    n = search_value_bst(root, "둘");  print_node("srch 둘 : ", n)
    n = search_value_bst(root, "열");  print_node("srch 열 : ", n)

    root = delete_bst(root, 7);  print_tree("del 7 : ", root)
    root = delete_bst(root, 8);  print_tree("del 8 : ", root)
    root = delete_bst(root, 2);  print_tree("del 2 : ", root)
    root = delete_bst(root, 6);  print_tree("del 6 : ", root)