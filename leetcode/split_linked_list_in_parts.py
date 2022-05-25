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
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        splits = []
        total = 0
        h = head
        while h is not None:
            total += 1
            h = h.next

        ans = int(total / k)
        quo = total % k
        for i in range(k):
            val = ans
            if quo > 0:
                quo -= 1
                val += 1
            splits.append(val)
        ll = []
        h = head
        for i in splits:
            ll.append(h)
            for j in range(i-1):
                h = h.next
            if h is None:
                h = None
                continue
            h1 = h.next
            h.next = None
            h = h1
        return ll


def constructLinkedList(list: List[int]) -> Optional[ListNode]:
    ll = ListNode(list[0])
    head = ll
    for index in range(1, len(list)):
        node = ListNode(list[index], None)
        head.next = node
        head = node
    return ll


if __name__ == '__main__':
    l = [1]
    ll = constructLinkedList(l)
    k = 13
    res = Solution().splitListToParts(ll, k)
    for l in res:
        if l is None:
            print(None)
            continue
        l.print()
    # print(res)
