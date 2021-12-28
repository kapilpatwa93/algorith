# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.recurse(root1, root2)

    def recurse(self, subRoot1: Optional[TreeNode], subRoot2: Optional[TreeNode]) -> Optional[TreeNode]:
        if subRoot1 is None and subRoot2 is None:
            return None
        node = TreeNode()
        val = 0
        left1 = None
        left2 = None
        right1, right2 = None, None
        if subRoot1 is not None:
            val += subRoot1.val
            left1 = subRoot1.left
            right1 = subRoot1.right
        if subRoot2 is not None:
            val += subRoot2.val
            left2 = subRoot2.left
            right2 = subRoot2.right
        node.val = val
        node.left = self.recurse(left1, left2)
        node.right = self.recurse(right1, right2)
        return node


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
    list1 = [1, 2, 2, 3, 3, 3, 3, 4]
    list2 = [1]
    tree1 = getTree(list1)
    tree2 = getTree(list2)
    res = Solution().mergeTrees(tree1, tree2)
    print(res)
