# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.recursivecount(1, root)

    def recursivecount(self, count, subRoot: Optional[TreeNode]) -> int:
        if subRoot is None:
            return count
        if subRoot.right is None and subRoot.left is None:
            return count
        if subRoot.right is None:
            return count * 2
        m1 = self.recursivecount(count * 2, subRoot.left)
        m2 = self.recursivecount((count * 2) + 1, subRoot.right)
        return max(m1, m2)


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
    list = [1, 2, 3, 4]
    tree = getTree(list)
    res = Solution().countNodes(tree)
    print(res)
