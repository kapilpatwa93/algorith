from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def isLeaf(subroot) -> bool:
            return not subroot.left and not subroot.right

        def recurse(subroot, nums) -> int:
            if subroot is None:
                return 0
            if isLeaf(subroot):
                return (nums * 10 + subroot.val)

            nums = (nums * 10) + subroot.val
            return recurse(subroot.left, nums) + recurse(subroot.right, nums)

        return recurse(root, 0)
