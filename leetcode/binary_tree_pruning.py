# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(subroot: TreeNode) -> TreeNode:
            if subroot is None:
                return None
            subroot.left = recurse(subroot.left)
            subroot.right = recurse(subroot.right)
            if subroot.val == 0 and (subroot.left is None and subroot.right is None):
                return None
            else:
                return subroot

        return recurse(root)
