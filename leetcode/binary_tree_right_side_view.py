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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView = []

        def recurse(subroot: TreeNode, level: int):
            if subroot is None:
                return
            if len(rightView) <= level:
                rightView.append(subroot.val)
            recurse(subroot.right, level + 1)
            recurse(subroot.left, level + 1)
            return

        recurse(root, 0)
        return rightView


if __name__ == '__main__':
    list = []

    tree = getTree(list)
    res = Solution().rightSideView(tree)
    print(res)
