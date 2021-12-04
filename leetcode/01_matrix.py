from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        return self.recursive(mat)

    memo = []
    high = 0
    inProgress = []

    def recursive(self, mat):
        self.high = max(len(mat), len(mat[0]))
        self.memo = [[None for _ in range(len(mat[0]))] for _ in range(len(mat))]
        self.inProgress = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]

        def recurse(x, y, isCurr):
            if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]):
                return self.high

            if self.inProgress[x][y] is True and isCurr is False:
                return self.high
            self.inProgress[x][y] = True

            num = mat[x][y]
            if num == 0:
                self.memo[x][y] = 0
                self.inProgress[x][y] = False
                return self.memo[x][y]

            if self.memo[x][y] is not None and isCurr is False:
                self.inProgress[x][y] = False
                return self.memo[x][y]

            self.memo[x][y] = min(
                recurse(x + 1, y, False),
                recurse(x, y + 1, False),
                recurse(x - 1, y, False),
                recurse(x, y - 1, False),
            ) + 1
            self.inProgress[x][y] = False
            return self.memo[x][y]

        for x in range(len(mat)):
            for y in range(len(mat[0])):
                self.inProgress[x][y] = True
                self.memo[x][y] = recurse(x, y, True)
                self.inProgress[x][y] = False

        for x in reversed(range(len(mat))):
            for y in reversed(range(len(mat[0]))):
                self.inProgress[x][y] = True
                self.memo[x][y] = recurse(x, y, True)
                self.inProgress[x][y] = False
        return self.memo


if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
           [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 0, 0]]
    res = Solution().updateMatrix(mat)
    print(res)
