from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def isLeaf(xStart, xEnd, yStart, yEnd):
            val = grid[yStart][xStart]
            for x in range(xStart, xEnd + 1):
                for y in range(yStart, yEnd + 1):
                    if val != grid[y][x]:
                        return False
            return True

        # only for isLeaf
        def getVal(xStart, xEnd, yStart, yEnd):
            return grid[yStart][xStart]

        def recurse(xStart, xEnd, yStart, yEnd) -> Node:
            leaf = isLeaf(xStart, xEnd, yStart, yEnd)

            val = 1
            if leaf:
                val = getVal(xStart, xEnd, yStart, yEnd)
                return Node(val, leaf, None, None, None, None)

            xMid = int((xStart + xEnd) / 2)
            yMid = int((yStart + yEnd) / 2)

            topLeft = recurse(xStart, xMid, yStart, yMid)
            topRight = recurse(xMid + 1, xEnd, yStart, yMid)
            bottomLeft = recurse(xStart, xMid, yMid + 1, yEnd)
            bottomRight = recurse(xMid + 1, xEnd, yMid + 1, yEnd)

            return Node(val, leaf, topLeft, topRight, bottomLeft, bottomRight)

        return recurse(0, len(grid) - 1, 0, len(grid) - 1)


if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0]]

    res = Solution().construct(grid)
    print(res)
