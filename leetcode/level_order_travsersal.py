# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        def recurse(subroot: Optional[TreeNode], level):
            if subroot is None:
                return
            if level >= len(levels):
                levelArr = []
                levels.append(levelArr)

            levels[level].append(subroot.val)
            recurse(subroot.left, level + 1)
            recurse(subroot.right, level + 1)
            return

        recurse(root, 0)
        return levels


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
    nodes = [3, 9, 20, None, None, 15, 7]
    # nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    tree = getTree(nodes)
    res = Solution().levelOrder(tree)
    print(res)
