from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def hasChild(subroot: 'Node') -> bool:
            return subroot.left if subroot.left is not None else subroot.right is not None

        def recurse(subroot: 'Node', next: Optional[Node]):
            if subroot is None:
                return subroot
            subroot.next = next
            extremeRight = None
            tempNext = subroot.next
            while tempNext is not None:
                if hasChild(tempNext):
                    break
                tempNext = tempNext.next

            if tempNext is not None:
                extremeRight = tempNext.left if tempNext.left is not None else tempNext.right
            if subroot.right is not None:
                subroot.right = recurse(subroot.right, extremeRight)
                subroot.left = recurse(subroot.left, subroot.right)
            else:
                subroot.left = recurse(subroot.left, extremeRight)
            return subroot

        return recurse(root, None)


def getTree(nodes: List[int]) -> Node:
    def recurse(index):
        if index >= len(nodes):
            return None
        if nodes[index] is None:
            return None
        subroot = Node(nodes[index])
        left = recurse((index * 2) + 1)
        right = recurse((index * 2) + 2)
        subroot.left = left
        subroot.right = right
        return subroot

    return recurse(0)


if __name__ == '__main__':
    # list = [1, 2, 3, 4, 5, None, 7]
    # list = [1, 2, 3, 4, None, None, 5, 6, None, None, None, None, None, None, 7]
    list = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, None, None, 8]
    tree = getTree(list)
    res = Solution().connect(tree)
    print(res)
