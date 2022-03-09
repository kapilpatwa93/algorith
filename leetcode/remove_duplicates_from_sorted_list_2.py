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


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        prev = None
        while h is not None:
            if h.next is not None and h.next.val == h.val:
                h2 = h
                while h is not None and h2.val == h.val:
                    h = h.next
                if prev is None:
                    head = h
                else:
                    prev.next = h
            else:
                prev = h
                h = h.next
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
    nums = [1, 2, 3, 4, 5, 5, 5]
    ll = constructLinkedList(nums)
    res = Solution().deleteDuplicates(ll)
    res.print()
