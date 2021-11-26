from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        def getCellValue(x: int, y: int) -> int:
            if x < 0 or y < 0 or x >= row or y >= col:
                return 0
            return grid[x][y]

        def findArea(i, j) -> int:
            queue = [[i, j]]
            index = 0
            while index < len(queue):
                x = queue[index][0]
                y = queue[index][1]
                visited[x][y] = True
                if getCellValue(x + 1, y) == 1 and not visited[x + 1][y]:
                    visited[x + 1][y] = True
                    queue.append([x + 1, y])
                if getCellValue(x - 1, y) == 1 and not visited[x - 1][y]:
                    visited[x - 1][y] = True
                    queue.append([x - 1, y])
                if getCellValue(x, y + 1) == 1 and not visited[x][y + 1]:
                    visited[x][y + 1] = True
                    queue.append([x, y + 1])
                if getCellValue(x, y - 1) == 1 and not visited[x][y - 1]:
                    visited[x][y - 1] = True
                    queue.append([x, y - 1])
                index += 1
            return len(queue)

        maxArea = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == 1:
                    maxArea = max(maxArea, findArea(i, j))
        return maxArea


def main():
    image = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    image = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    res = Solution().maxAreaOfIsland(image, )
    print(res)


main()
