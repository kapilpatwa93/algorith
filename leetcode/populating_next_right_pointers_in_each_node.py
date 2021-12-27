"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.recurse(root, None)
        return root

    def recurse(self, left: 'Optional[Node]', right: 'Optional[Node]') -> 'Optional[Node]':
        if left is None:
            return

        if left.left is not None:
            left.left.next = left.right
        self.recurse(left.left, left.right)

        if right is None:
            return

        if right.left is not None:
            right.left.next = right.right

        if left.right is not None:
            left.right.next = right.left

        self.recurse(right.left, right.right)
        self.recurse(left.right, right.left)


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
        subroot.next = None
        return subroot

    return recurse(0)


if __name__ == '__main__':
    list = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    tree = getTree(list)
    res = Solution().connect(tree)
    print(res)
