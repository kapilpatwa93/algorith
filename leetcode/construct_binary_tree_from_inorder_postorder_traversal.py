# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def recurse(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            if len(inorder) == 0:
                return None
            rootVal = postorder[-1]

            node = TreeNode(rootVal)
            i = inorder.index(rootVal)

            node.left = recurse(inorder[:i], postorder[:i])
            node.right = recurse(inorder[i + 1:], postorder[i:-1])
            return node

        return recurse(inorder, postorder)
