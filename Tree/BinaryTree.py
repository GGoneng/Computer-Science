from ArrayQueue import ArrayQueue

class BTNode:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

def preorder(n):
    if n is not None:
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=" ")
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=" ")

def levelorder(root):
    queue = ArrayQueue()
    queue.enqueue(root)
    
    while not queue.isEmpty(): 
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=" ")
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return count_node(n.left) + count_node(n.right) + 1
    
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1