from typing import List, Union, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
    pPath = []
    qPath = []
    commonNode = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pPath = []
        self.qPath = []

        def recurse(subroot: TreeNode) -> tuple[bool, bool]:
            if subroot is None:
                return False, False
            foundP = False
            foundQ = False

            if subroot.val == p.val:
                foundP = True

            if subroot.val == q.val:
                foundQ = True

            res1 = recurse(subroot.left)
            res2 = recurse(subroot.right)
            foundP1, foundQ1 = res1[0], res1[1]
            foundP2, foundQ2 = res2[0], res2[1]
            if self.commonNode is None and ((foundP or foundP1 or foundP2) and (foundQ or foundQ1 or foundQ2)):
                self.commonNode = subroot

            return foundP or foundP1 or foundP1, foundQ or foundQ1 or foundQ2

        recurse(root)
        return self.commonNode


class Solution1:
    pPath = []
    qPath = []
    commonNode = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pPath = []
        self.qPath = []
        self.commonNode = None

        def recurse(subroot: TreeNode, path: List[int]):
            if subroot is None:
                return
            path = path.copy()
            path.append(subroot.val)
            if subroot.val == p.val:
                self.pPath = path.copy()

            if subroot.val == q.val:
                self.qPath = path.copy()

            recurse(subroot.left, path)
            recurse(subroot.right, path)

        recurse(root, [])
        i = 0
        j = 0
        common = self.pPath[0]
        while i < len(self.pPath) and j < len(self.qPath):
            if self.pPath[i] == self.qPath[j]:
                common = self.pPath[i]
            i += 1
            j += 1

        def find(subroot: TreeNode) -> TreeNode:
            if subroot is None:
                return
            if subroot.val == common:
                self.commonNode = subroot
                return
            find(subroot.left)
            find(subroot.right)

        find(root)
        return self.commonNode


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    p = TreeNode(1)
    q = TreeNode(2)
    tree = getTree(list)
    res = Solution().lowestCommonAncestor(tree, p, q)
    print(res.val)
