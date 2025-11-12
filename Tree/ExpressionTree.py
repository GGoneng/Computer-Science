from BinaryTree import *

def evaluate(node):
    if node is None:
        return 0
    
    elif node.isLeaf():
        return node.data
    
    else:
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)

        if node.data == '+': return op1 + op2
        elif node.data == '-': return op1 - op2
        elif node.data == '*': return op1 * op2
        elif node.data == '/': return op1 / op2

def buildETree(expr):
    if len(expr) == 0:
        return None
    
    token = expr.pop()
    if token in "+-*/":
        node = BTNode(token)
        node.right = buildETree(expr)
        node.left = buildETree(expr)
        return node
    else:
        return BTNode(float(token))
    
if __name__ == "__main__":
    str = input("입력(후위표기) : ")
    expr = str.split()

    print("토큰분리 (expr) : ", expr)

    root = buildETree(expr)

    print("\n 전위순회: ", end=''); preorder(root)
    print("\n 중위순회: ", end=''); inorder(root)
    print("\n 후위순회: ", end=''); postorder(root)
    print("\n 계산 결과 : ", evaluate(root))