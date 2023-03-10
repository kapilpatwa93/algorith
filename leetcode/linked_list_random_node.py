from random import random
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    curr = None
    head = None

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.curr = head

    def getRandom(self) -> int:
        h = self.head
        count = 0
        result = None
        while h:
            count += 1
            randVal = random.randint(1, count)
            if randVal == 1:
                result = h.val
            h = h.next
        return result
