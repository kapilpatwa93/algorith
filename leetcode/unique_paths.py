class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n] * m
        grid[0][0] = 1
        def getCell(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            return grid[i][j]
        for i in range(m):
            for j in range(n):
                grid[i][j] = max(grid[i][j],getCell(i-1,j) + getCell(i,j-1))
        return grid[m-1][n-1]

if __name__ == '__main__':
    m = 3
    n = 7
    res = Solution().uniquePaths(m,n)
    print(res)