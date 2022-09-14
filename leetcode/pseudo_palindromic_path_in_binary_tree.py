# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total = 0

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def isLeaf(subroot: TreeNode) -> bool:
            return subroot.left is None and subroot.right is None

        def isPseudoPalindrome(countArr: List[int]) -> bool:
            oddCount, evenCount = 0, 0
            for i in countArr:
                if i % 2 == 0:
                    evenCount += 1
                else:
                    oddCount += 1
            return oddCount <= 1

        countArr = [0] * 10

        def recurse(subroot: TreeNode, countArr: List[int]):
            if subroot is None:
                return

            countArr[subroot.val] += 1

            if isLeaf(subroot):
                self.total += 1 if isPseudoPalindrome(countArr) else 0
            recurse(subroot.left, countArr.copy())
            recurse(subroot.right, countArr.copy())

        recurse(root, countArr)
        return self.total
