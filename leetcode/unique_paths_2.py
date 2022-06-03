from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        count = [[0 if cell == 0 else 0 for cell in row] for row in obstacleGrid]

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        count[rows - 1][cols - 1] = 1
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        def getVal(i, j):
            if i >= rows or j >= cols:
                return 0
            return count[i][j]

        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if obstacleGrid[i][j] == 0:
                    count[i][j] = getVal(i + 1, j) + getVal(i, j + 1)
                if i == rows - 1 and j == cols - 1:
                    count[i][j] = 1
        return count[0][0]


if __name__ == '__main__':
    path = [
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    res = Solution().uniquePathsWithObstacles(path)
    print(res)
