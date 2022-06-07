# Definition for a binary tree node.
from typing import List, Optional


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
    sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def isLeaf(subroot: TreeNode) -> bool:
            return subroot is not None and subroot.left is None and subroot.right is None

        def recurse(subroot: TreeNode, number: int):
            if subroot is None:
                return
            number = (number * 10) + subroot.val
            if isLeaf(subroot):
                self.sum += number
            recurse(subroot.left, number)
            recurse(subroot.right, number)

        recurse(root, 0)
        return self.sum


if __name__ == '__main__':
    list = [4, 9, None, 5, 1]
    tree = getTree(list)
    res = Solution().sumNumbers(tree)
    print(res)
