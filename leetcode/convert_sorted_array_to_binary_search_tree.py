from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(arr: List[int]) -> Optional[TreeNode]:
            if len(arr) == 0:
                return None
            mid = int(len(arr) / 2)
            subroot = TreeNode(arr[mid])
            subroot.left = construct(arr[:mid])
            subroot.right = construct(arr[mid + 1:])
            return subroot

        return construct(nums)


if __name__ == '__main__':
    nums = [3, 5, 7, 10, 12, 15, 20]
    res = Solution().sortedArrayToBST(nums)
    print(res)
