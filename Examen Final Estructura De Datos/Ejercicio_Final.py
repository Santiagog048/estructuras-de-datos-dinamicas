from collections import deque

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(tree, callback):
    stack = deque()
    current = tree

    while stack or current:
        if current:
            stack.appendleft(current)
            current = current.left
        else:
            current = stack.popleft()
            callback(current.value)
            current = current.right

# Ejemplo de uso
def someCallback(value):
    print(f"callback({value})")

tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
tree.left.left = BinaryTree(4)
tree.left.left.right = BinaryTree(9)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)

in_order_traversal(tree, someCallback)