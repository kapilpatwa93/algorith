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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        head = None
        p3 = head
        prev = None
        carry = 0
        while p1 is not None or p2 is not None or carry > 0:
            val = 0
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            if carry > 0:
                val += carry

            # if val > 9:
            carry = int(val / 10)
            val = val % 10
            # else
            # print(val,carry)
            if head is None:
                head = ListNode(val)
                prev = head
                # p3 = head.next
            else:
                prev.next = ListNode(val)
                prev = prev.next

        return head


if __name__ == '__main__':
    l1 = [1, 2, 3, 4]
    l2 = [9, 9, 9, 9, 9]
    list1 = constructLinkedList(l1)
    list2 = constructLinkedList(l2)
    res = Solution().addTwoNumbers(list1, list2)
    res.print()
