# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    minDistance = 100000
    prev = 0

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.minDistance = 1000000
        self.prev = -1

        def traverse(subroot: TreeNode):
            if subroot is None:
                return
            traverse(subroot.left)
            if self.prev != -1:
                self.minDistance = min(self.minDistance, subroot.val - self.prev)
            self.prev = subroot.val
            traverse(subroot.right)

        traverse(root)
        return self.minDistance
