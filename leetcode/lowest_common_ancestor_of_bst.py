# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        def recurse(subroot: TreeNode):
            if p.val <= subroot.val <= q.val:
                return subroot
            if subroot.val > p.val and subroot.val > q.val:
                return recurse(subroot.left)
            return recurse(subroot.right)

        return recurse(root)

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.node = None

        def recurse(subroot: TreeNode) -> (bool, bool):
            if subroot is None:
                return (False, False)

            fp, fq = False, False
            if subroot.val == p.val:
                fp = True
            if subroot.val == q.val:
                fq = True

            flp, flq = recurse(subroot.left)
            frp, frq = recurse(subroot.right)

            if (fp or frp or flp) and (fq or frq or flq) and self.node is None:
                self.node = subroot

            return (fp or frp or flp, fq or frq or flq)

        recurse(root)
        return self.node


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
    list = [100, 50, 200, 25, 75, 150, 250]
    p = TreeNode(50)
    q = TreeNode(25)
    tree = getTree(list)
    res = Solution().lowestCommonAncestor(tree, p, q)
    print(res.val)
