# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, 0)

    def recurse(self, subroot: TreeNode, currentDepth):
        if subroot is None:
            return currentDepth
        return max(self.recurse(subroot.left, currentDepth + 1), self.recurse(subroot.right, currentDepth + 1))


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
    list = [1, 2, 2, 3, 3, 3, 3,4]
    tree = getTree(list)
    res = Solution().maxDepth(tree)
    print(res)
