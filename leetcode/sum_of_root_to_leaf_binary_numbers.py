from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.recurse(root, 0)
        return self.total

    def recurse(self, subroot: TreeNode, total: int):
        if subroot is None:
            return

        total = total * 2 + subroot.val
        if subroot.left is None and subroot.right is None:
            self.total += total
            return
        self.recurse(subroot.left, total)
        self.recurse(subroot.right, total)


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
    list = [1, 0, 1, 0, 1, 0, 1]
    tree = getTree(list)
    res = Solution().sumRootToLeaf(tree)
    print(res)
