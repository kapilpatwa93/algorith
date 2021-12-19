# Definition for singly-linked list.
from typing import Optional, List


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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        prev = None
        p2 = head

        for _ in range(1, n):
            p2 = p2.next

        while p2.next is not None:
            p2 = p2.next
            prev = p1
            p1 = p1.next

        if prev is None:
            head = head.next
            return head
        else:
            prev.next = prev.next.next
        return head


def constructLinkedList(list: List[int]) -> Optional[ListNode]:
    ll = ListNode(list[0])
    head = ll
    for index in range(1, len(list)):
        node = ListNode(list[index], None)
        head.next = node
        head = node
    return ll


if __name__ == '__main__':
    list = [1, 2, 3, 4]
    n = 2
    ll = constructLinkedList(list)
    res = Solution().removeNthFromEnd(ll, n)
    if res is not None:
        res.print()
