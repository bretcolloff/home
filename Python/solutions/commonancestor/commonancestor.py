import os, sys
lib_path = os.path.abspath(os.path.join('..', '..'))
sys.path.append(lib_path)
from lib.bst import BSTNode

def commonAncestor(node, a, b):
    left = node.left.haschild(a) or node.left.haschild(b)
    right = node.right.haschild(a) or node.right.haschild(b)

    if left and right:
        return node
    elif left:
        return commonAncestor(node.left, a, b)
    else:
        return commonAncestor(node.right, a, b)

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

    #                     5
    #                   /   \
    #                  3      8
    #                /  \   /  \
    #              1    4  6    9
    #            /  \       \    \
    #          0     2       7    10

    print(root.haschild(4))
    print(root.haschild(11))

    common = commonAncestor(root, 2, 4)
    print (common.value)
    common = commonAncestor(root, 0, 10)
    print (common.value)

if __name__ == '__main__':
    main()
