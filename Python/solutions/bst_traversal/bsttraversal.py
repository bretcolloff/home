import os, sys
lib_path = os.path.abspath(os.path.join('..', '..'))
sys.path.append(lib_path)
from lib.bst import BSTNode
from collections import deque

def inordertraversal(root):
    if root.left is not None:
        inordertraversal(root.left)
    print(root.value)
    if root.right is not None:
        inordertraversal(root.right)

def bottomup(root):
    stack = []
    # append, popleft
    queue = deque()
    queue.append(root)

    while queue:
        n = queue.popleft()
        stack.append(n)
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)

    while stack:
        n = stack.pop()
        print (n.value)

def main(argv=None):
    root = BSTNode(5)
    # Populate tree
    root.add(BSTNode(3))
    root.add(BSTNode(8))
    root.add(BSTNode(1))
    root.add(BSTNode(2))
    root.add(BSTNode(4))
    root.add(BSTNode(6))
    root.add(BSTNode(7))
    root.add(BSTNode(9))
    root.add(BSTNode(10))
    root.add(BSTNode(0))

    inordertraversal(root)
    bottomup(root)
    #                     5
    #                   /   \
    #                  3      8
    #                /  \   /  \
    #              1    4  6    9
    #            /  \       \    \
    #          0     2       7    10

if __name__ == '__main__':
    main()
