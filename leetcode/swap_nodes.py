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


from typing import Optional, List


class Solution:
    class Solution:
        def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            frontPointer = head
            p2 = head
            for index in range(1, k):
                frontPointer = frontPointer.next
            p1 = frontPointer
            if frontPointer.next is None:
                p2 = head

            while frontPointer.next is not None:
                frontPointer = frontPointer.next
                p2 = p2.next

            p2.val, p1.val = p1.val, p2.val
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
    for index in range(1, 2):
        print(index)
    list = [1, 2, 3, 4]
    n = 2
    ll = constructLinkedList(list)
    res = Solution().swapNodes(ll, n)
    if res is not None:
        res.print()
