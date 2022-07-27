# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def recurse(subroot: TreeNode, right: Optional[TreeNode], isLeft: bool) -> Optional[TreeNode]:
            if subroot is None:
                return None

            res = recurse(subroot.right, right, False)
            if res is None:
                subroot.right = right

            recurse(subroot.left, subroot.right, True)

            if subroot.left is not None:
                subroot.right = subroot.left
                subroot.left = None

            return subroot

        recurse(root, None, False)


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
    list = [1, 2, 3, 4, 5, 6, 7, None, None, None, None, 8, 9, None, None]
    tree = getTree(list)
    Solution().flatten(tree)
    print(tree)
