# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []
        h = head
        i = 0

        def removeFromStack(v: (int, int)):
            while len(stack) > 0 and v[0] > stack[-1][0]:
                popped = stack.pop()
                ans[popped[1]] = v[0]
            stack.append(v)

        while h is not None:
            if len(stack) > 0 and h.val < stack[-1][0]:
                stack.append((h.val, i))
            else:
                removeFromStack((h.val, i))
            h = h.next
            i += 1
            ans.append(0)

        return ans


def constructLinkedList(list: List[int]) -> Optional[ListNode]:
    ll = ListNode(list[0])
    head = ll
    for index in range(1, len(list)):
        node = ListNode(list[index], None)
        head.next = node
        head = node
    return ll


if __name__ == '__main__':
    list = [1,2,3,4,5,4,3,2,1,1,2,3,4,6,45,3]
    n = 2
    ll = constructLinkedList(list)
    res = Solution().nextLargerNodes(ll)
    print(list)
    print(res)
