# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def traverse(subroot1: TreeNode, subroot2: TreeNode):
            if subroot1 is None and subroot2 is None:
                return True
            elif subroot1 is None:
                return False
            elif subroot2 is None:
                return False
            if subroot1.val != subroot2.val:
                return False
            return traverse(subroot1.right, subroot2.left) and traverse(subroot1.left, subroot2.right)

        return traverse(root, root)


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


if __name__ == '__main__':
    list = [1, 2, 2]
    tree = getTree(list)
    res = Solution().isSymmetric(tree)
    print(res)
