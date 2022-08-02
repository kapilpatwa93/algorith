from typing import Optional, List


# Definition for singly-linked list.
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total = 0
        start = head
        p1 = head
        while start is not None:
            total += 1
            start = start.next
        if total == 0:
            return head
        k = k % total
        if k == total or k == 0:
            return head
        move = total - k
        while move > 1:
            p1 = p1.next
            move = move - 1
        p2 = p1
        newHead = p1.next
        while p2.next is not None:
            p2 = p2.next

        p2.next = head
        p1.next = None
        return newHead


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    k = 2
    ll = constructLinkedList(l)
    res = Solution().rotateRight(ll, k)
    res.print()
