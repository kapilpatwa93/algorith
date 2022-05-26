# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    smallest = None

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.smallest = None

        def recurse(subroot: TreeNode, s: str):
            if subroot is None:
                return
            s1 = chr(97 + subroot.val) + s
            if subroot.left is None and subroot.right is None:
                if self.smallest is None:
                    self.smallest = s1
                if s1 < self.smallest:
                    self.smallest = s1
                return
            recurse(subroot.left, s1)
            recurse(subroot.right, s1)
            return

        recurse(root, "")
        return self.smallest

