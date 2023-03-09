# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        p1 = head
        p2 = head
        if not head:
            return None
        while p1 and p2:
            if not p1.next:
                return None
            if  not p2 or not p2.next or not p2.next.next:
                return None
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                while h != p2:
                    h = h.next
                    p2 = p2.next
                return h
        return None

