# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root)

    lastVal = None

    def recurse(self, subRoot: TreeNode):
        if subRoot is None:
            return True
        isLeftValid = self.recurse(subRoot.left)
        if self.lastVal is None:
            isMidValid = True
        else:
            isMidValid = self.lastVal < subRoot.val
        self.lastVal = subRoot.val

        isRightValid = self.recurse(subRoot.right)
        return isRightValid and isLeftValid and isMidValid


if __name__ == '__main__':
    # list = [4, 2, 6, 1, 3, 5, 7]
    list = [0, -1]
    # list = [5, 4, 6, None, None, 3, 6]
    tree = getTree(list)
    res = Solution().isValidBST(tree)
    print(res)
