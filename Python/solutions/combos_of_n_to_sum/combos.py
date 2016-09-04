import os, sys
lib_path = os.path.abspath(os.path.join('..', '..'))
sys.path.append(lib_path)
from lib.bst import BSTNode

def main(argv=None):
    numbers = [5, 3, 8, 1, 2, 4, 6, 7, 9, 10, 0]
    total = 12
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

    combos = []

    for n in numbers:
        if n >= total:
            continue
        rem = total - n
        if root.haschild(rem):
            combos.append([n, rem])

    for c in combos:
        print (c)

if __name__ == '__main__':
    main()
