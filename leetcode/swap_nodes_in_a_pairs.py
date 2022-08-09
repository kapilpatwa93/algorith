# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        arr = []
        head = self
        while head is not None:
            arr.append(head.val)
            head = head.next
        print(arr)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recurse(head)

    def recurse(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head

        temp = head.next
        tempNext = head.next.next
        temp.next = head
        head.next = self.recurse(tempNext)
        return temp


def constructLinkedList(list: List[int]) -> Optional[ListNode]:
    if len(list) == 0:
        return None
    ll = ListNode(list[0])
    head = ll
    for index in range(1, len(list)):
        node = ListNode(list[index], None)
        head.next = node
        head = node
    return ll


if __name__ == '__main__':
    list = []
    n = 2
    ll = constructLinkedList(list)
    res = Solution().swapPairs(ll)
    if res is not None:
        res.print()
