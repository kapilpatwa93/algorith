# Definition for a binary tree node.
from math import inf
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getTree(nodes: List[int]) -> TreeNode:
    def recurse(index):
        if index >= len(nodes):
            return None
        if nodes[index] is None:
            return None
        subroot = TreeNode(nodes[index])
        left = recurse((index * 2) + 1)
        right = recurse((index * 2) + 2)
        subroot.left = left
        subroot.right = right
        return subroot

    return recurse(0)


class Solution:
    lastVal = 0

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.lastVal = -inf

        def recurse(subroot: Optional[TreeNode]) -> bool:
            if subroot is None:
                return True
            if not recurse(subroot.left):
                return False
            if subroot.val <= self.lastVal:
                return False
            self.lastVal = subroot.val
            return recurse(subroot.right)

        return recurse(root)


if __name__ == '__main__':
    # list = [4, 2, 6, 1, 3, 5, 7]
    list = [0, -1]
    # list = [5, 4, 6, None, None, 3, 6]
    tree = getTree(list)
    res = Solution().isValidBST(tree)
    print(res)
