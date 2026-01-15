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

    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    
    else:
        if root.left == None:
            return root.right
        
        if root.right == None:
            return root.left
        
        succ = root.right
        while succ.left != None:
            succ = succ.left

        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)
    
    return root