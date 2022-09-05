"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        node_queue = []
        res = []
        if root is None:
            return res

        node_queue.append((root, 0))

        for n in node_queue:
            (node, level) = n
            if node is not None:
                # print(level, res, node.val)
                if len(res) <= level:
                    res.append([node.val])
                else:
                    res[level].append(node.val)

                for c in node.children:
                    node_queue.append((c, level + 1))

        return res
