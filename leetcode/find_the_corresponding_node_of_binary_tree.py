# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def recurse(subroot1: TreeNode, subroot2: TreeNode) -> TreeNode:
            if subroot1 is None:
                return None
            if subroot1 is target:
                return subroot2

            left = recurse(subroot1.left, subroot2.left)
            if left is not None:
                return left
            return recurse(subroot1.right, subroot2.right)

        return recurse(original, cloned)
