# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    maxDepth = 0
    res = None
    def findAllSubTreePath(self, subroot: TreeNode, dist: int):
        if subroot is None:
            if dist > self.maxDepth:
                self.maxDepth = dist
            return dist

        r1 = self.findAllSubTreePath(subroot.left, dist + 1)
        r2 = self.findAllSubTreePath(subroot.right, dist + 1)
        if r1 == r2 and r1 == self.maxDepth:
            self.res = subroot
        return max(r1, r2)

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.res = None
        self.maxDepth = 0
        self.findAllSubTreePath(root, 0)
        return self.res


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
    list = [0, 1, 2, 3, 4, None, None, 7, 8, 9, None, None, None, None]
    tree = getTree(list)
    res = Solution().subtreeWithAllDeepest(tree)
    print(res.val)
