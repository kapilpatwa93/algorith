from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}
        h = head
        prev = None
        newH = None
        while h is not None:

            if h in nodeMap:
                newHead = nodeMap[h]
            else:
                newHead = Node(h.val)
                nodeMap[h] = newHead

            if newH is None:
                newH = newHead

            if prev is not None:
                prev.next = newHead

            if h.random is not None:
                if h.random not in nodeMap:
                    nodeMap[h.random] = Node(h.random.val)
                newHead.random = nodeMap[h.random]

            prev = newHead
            h = h.next
        return newH
