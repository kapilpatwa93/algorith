# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def constructLinkedList(list: List[int]) -> Optional[ListNode]:
    ll = ListNode(list[0])
    head = ll
    for index in range(1, len(list)):
        node = ListNode(list[index], None)
        head.next = node
        head = node
    return ll


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def nextDirection(currentDirection: str) -> str:
            if currentDirection == 'u':
                return 'r'
            elif currentDirection == 'r':
                return 'd'
            elif currentDirection == 'd':
                return 'l'
            else:
                return 'u'

        def isValid(newX: int, newY: int) -> bool:
            if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[0]):
                return False
            return grid[newX][newY] is None

        def newXY(currentDirection: str, x: int, y: int) -> (int, int):
            if currentDirection == 'u':
                return x - 1, y
            elif currentDirection == 'r':
                return x, y + 1
            elif currentDirection == 'd':
                return x + 1, y
            else:
                return x, y - 1

        currentX = 0
        currentY = -1
        direction = "r"
        grid = [[None for _ in range(n)] for _ in range(m)]
        h = head
        for i in range(m * n):
            newX, newY = newXY(direction, currentX, currentY)
            if not isValid(newX, newY):
                direction = nextDirection(direction)
                newX, newY = newXY(direction, currentX, currentY)
            if h is not None:
                grid[newX][newY] = h.val
            else:
                grid[newX][newY] = -1
            currentX, currentY = newX, newY
            if h is not None:
                h = h.next

        return grid


if __name__ == '__main__':
    nums = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
    m = 3
    n = 5
    ll = constructLinkedList(nums)
    res = Solution().spiralMatrix(m, n, ll)
    for r in res:
        print(r)
