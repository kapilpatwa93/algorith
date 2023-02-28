# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        preMap = defaultdict(lambda: 0)

        sol = []
        solMap = {}

        def recurse(subroot) -> str:
            if subroot is None:
                return ""
            pre = str(subroot.val) + "L" + recurse(subroot.left) + "R" + recurse(subroot.right)
            preMap[pre] += 1
            if pre in preMap and preMap[pre] == 2:
                sol.append(subroot)
            return pre

        recurse(root)
        return sol