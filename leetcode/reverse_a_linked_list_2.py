from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        newHead = None
        count = 1
        pointer = head
        leftPointer = None

        # traverse before left
        while count < left:
            leftPointer = pointer
            pointer = pointer.next
            count += 1
        reverseCounter = 1
        rightPointer = None

        # reverse the elements between left and right
        while pointer is not None and reverseCounter <= (right - left) + 1:

            prev = ListNode()

            if not newHead:
                newHead = ListNode(pointer.val)
                # assign the last element of list(after reversal) as right pointer
                rightPointer = newHead
            else:
                newHead.val = pointer.val

            prev.next = newHead
            newHead = prev
            pointer = pointer.next
            reverseCounter += 1
        # assign the remaining list to the next of the right pointer
        if rightPointer:
            rightPointer.next = pointer

        # return the left list is None then assign the start of reversed list as head
        if not leftPointer:
            return newHead.next

        # assign the reversed list to the next of the left pointer
        if leftPointer and newHead:
            leftPointer.next = newHead.next

        return head


def constructLinkedList(list: List[int]) -> Optional[ListNode]:
    ll = ListNode(list[0])
    head = ll
    for index in range(1, len(list)):
        node = ListNode(list[index], None)
        head.next = node
        head = node
    return ll


def main():
    list = [1, 2, 3, 4, 5]
    linkedList = constructLinkedList(list)
    res = Solution().reverseBetween(linkedList, 1, 3)
    print(res)


main()
