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


def constructLinkedList(l: List[int]) -> Optional[ListNode]:
    ll = ListNode(l[0])
    head = ll
    for index in range(1, len(l)):
        node = ListNode(l[index], None)
        head.next = node
        head = node
    return ll


def linkedListSum(l: ListNode) -> List[int]:
    h = l
    head = l
    prevHead = None
    newHead = l
    totalCount = 0

    while h is not None:
        totalCount += 1
        h = h.next
    nc = 0
    while head is not None:
        newHead = head
        head = head.next
        if nc >= (totalCount / 2):
            newHead.next = prevHead
            prevHead = newHead
        nc += 1
    rh = newHead
    res = []
    h = l
    while rh is not None:
        res.append(h.val + rh.val)
        h = h.next
        rh = rh.next
    return res


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    ll = constructLinkedList(l)
    res = linkedListSum(ll)
    print(res)
