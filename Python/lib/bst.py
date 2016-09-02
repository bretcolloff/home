
class BSTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def add(self, node):
        if node.value == self.value:
            return
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        if node.value > self.value:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)

    def haschild(self, value):
        exists = False
        if self.value is value:
            exists = True
        else:
            exists = exists if self.left is None else self.left.haschild(value)
            if exists is True:
                return exists
            exists = exists if self.right is None else self.right.haschild(value)
        return exists

def commonAncestor(node, a, b):
    left = node.left.haschild(a) or node.left.haschild(b)
    right = node.right.haschild(a) or node.right.haschild(b)

    if left and right:
        return node
    elif left:
        return commonAncestor(node.left, a, b)
    else:
        return commonAncestor(node.right, a, b)
