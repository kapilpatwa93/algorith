# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root
        subroot = root
        inserted = False
        while not inserted:
            if subroot.val > val:
                if subroot.left is None:
                    subroot.left = TreeNode(val)
                    inserted = True
                subroot = subroot.left
            else:
                if subroot.right is None:
                    subroot.right = TreeNode(val)
                    inserted = True
                subroot = subroot.right
        return root


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


if __name__ == '__main__':
    list = [40, 20, 60, 10, 30, 50, 70]
    val = 101
    tree = getTree(list)
    res = Solution().insertIntoBST(tree)
    print(res)
