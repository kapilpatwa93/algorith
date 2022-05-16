import math
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        distance = [[math.inf for _ in row] for row in grid]
        rows = len(grid) - 1
        cols = len(grid[0]) - 1
        distance[len(grid) - 1][len(grid[0]) - 1] = 0
        queue = [[rows, cols]]
        print(queue)

        def getCellValue(i, j):
            if i > rows or i < 0 or j > cols or j < 0:
                return math.inf
            if grid[i][j] == 0:
                return distance[i][j]
            else:
                return math.inf

        def getActualValue(i, j):
            if i > rows or i < 0 or j > cols or j < 0:
                return 1
            if grid[i][j] == 0:
                return grid[i][j]
            else:
                return 1

        def getMinimumAdjacent(i, j):
            return min(getCellValue(i, j + 1),
                       getCellValue(i, j - 1),
                       getCellValue(i - 1, j + 1),
                       getCellValue(i - 1, j - 1),
                       getCellValue(i - 1, j),
                       getCellValue(i + 1, j + 1),
                       getCellValue(i + 1, j - 1),
                       getCellValue(i + 1, j),

                       ) + 1

        for cell in queue:
            # ij = queue[i]
            i, j = cell[0], cell[1]
            if grid[i][j] == 0 and (distance[i][j] == math.inf or (i == rows and j == cols)):
                distance[i][j] = min(distance[i][j], getMinimumAdjacent(i, j))

                if getActualValue(i, j + 1) == 0:
                    queue.append([i, j + 1])
                if getActualValue(i, j - 1) == 0:
                    queue.append([i, j - 1])
                if getActualValue(i - 1, j + 1) == 0:
                    queue.append([i - 1, j + 1])
                if getActualValue(i - 1, j) == 0:
                    queue.append([i - 1, j])
                if getActualValue(i - 1, j - 1) == 0:
                    queue.append([i - 1, j - 1])
                if getActualValue(i + 1, j + 1) == 0:
                    queue.append([i + 1, j + 1])
                if getActualValue(i + 1, j) == 0:
                    queue.append([i + 1, j])
                if getActualValue(i + 1, j - 1) == 0:
                    queue.append([i + 1, j - 1])

        return -1 if distance[0][0] == math.inf else distance[0][0] + 1


if __name__ == '__main__':
    grid = [
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0]
    ]
    res = Solution().shortestPathBinaryMatrix(grid)
    print(res)
