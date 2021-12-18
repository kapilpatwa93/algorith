from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        initial = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    initial.append([i, j])

        queue.append(initial)
        count = 0

        def getVal(x, y) -> int:
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return 0
            return grid[x][y]

        while count < len(queue):
            for cells in queue:
                new = []
                for cell in cells:
                    x = cell[0]
                    y = cell[1]
                    if getVal(x + 1, y) == 1:
                        grid[x + 1][y] = 2
                        new.append([x + 1, y])
                    if getVal(x - 1, y) == 1:
                        grid[x - 1][y] = 2
                        new.append([x - 1, y])
                    if getVal(x, y - 1) == 1:
                        grid[x][y - 1] = 2
                        new.append([x, y - 1])
                    if getVal(x, y + 1) == 1:
                        grid[x][y + 1] = 2
                        new.append([x, y + 1])
                if len(new) > 0:
                    queue.append(new)
            count += 1
        ones = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones += 1
        return len(queue) - 1 if ones == 0 else -1


def main():
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    res = Solution().orangesRotting(grid)
    print(res)


main()
