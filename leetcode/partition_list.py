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


def constructLinkedList(list: List[int]) -> Optional[ListNode]:
    ll = ListNode(list[0])
    head = ll
    for index in range(1, len(list)):
        node = ListNode(list[index], None)
        head.next = node
        head = node
    return ll


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h = head
        p2Start = None
        p1Prev = None
        p2Prev = None
        p1Start = h
        while h is not None and h.val < x:
            p1Prev = h
            h = h.next

        while h is not None:
            if h.val < x:
                if p1Prev is None:
                    p1Prev = h
                    p1Start = p1Prev
                else:
                    p1Prev.next = h

                    p1Prev = p1Prev.next

                p2Prev.next = h.next
            else:
                if p2Start is None:
                    p2Start = h
                p2Prev = h

            h = h.next
        if p1Prev is not None:
            p1Prev.next = p2Start

        return p1Start


if __name__ == '__main__':
    l = [5, 6, 7, 2, 2, 4, 2, 2, 2, 3]
    x = 10
    ll = constructLinkedList(l)
    res = Solution().partition(ll, x)
    print(res.print())
