# Definition for singly-linked list.
from typing import Optional, List


# 1 2 3 4 5
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getNextToNext(node: ListNode):
            if node.next and node.next.next:
                return node.next.next
            return None

        stepper = head
        twoStepper = head
        while getNextToNext(twoStepper) is not None:
            twoStepper = getNextToNext(twoStepper)
            stepper = stepper.next

        if twoStepper.next is not None:
            stepper = stepper.next
        return stepper


def constructLinkedList(list: List[int]) -> Optional[ListNode]:
    ll = ListNode(list[0])
    head = ll
    for index in range(1, len(list)):
        node = ListNode(list[index], None)
        head.next = node
        head = node
    return ll


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]
    linkedList = constructLinkedList(list)
    res = Solution().middleNode(linkedList)
    print(res.val)
