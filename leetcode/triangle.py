from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.memo = []
        self.initMemo(triangle)
        return self.minimum(triangle, 0, 0)

    memo = []

    def initMemo(self, triangle: List[List[int]]):

        for row in triangle:
            self.memo.append([None for _ in range(len(row))])

    def minimum(self, triangle: List[List[int]], row, col) -> int:

        if row >= len(triangle) or col >= len(triangle[row]):
            return 0
        if self.memo[row][col] is not None:
            return self.memo[row][col]
        self.memo[row][col] = triangle[row][col] + min(self.minimum(triangle, row + 1, col),
                                                       self.minimum(triangle, row + 1, col + 1))
        return self.memo[row][col]


if __name__ == '__main__':
    list = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    res = Solution().minimumTotal(list)
    print(res)
