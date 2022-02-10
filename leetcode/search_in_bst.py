# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.traverse(root, val)

    def traverse(self, subroot: TreeNode, val: int):
        if subroot is None:
            return None

        if subroot.val == val:
            return subroot
        if subroot.val < val:
            return self.traverse(subroot.right, val)
        return self.traverse(subroot.left, val)


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
    list = [5, 2, 6, 1, 3, 5, 7]
    tree = getTree(list)
    res = Solution().searchBST(tree, 6)
    if res is not None:
        print(res.val)
    else:
        print(None)
