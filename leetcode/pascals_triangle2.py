from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [0] * (rowIndex + 1)

        arr[0] = 1

        def getVal(row, col):
            if row < 0 or row > rowIndex or col < 0 or col > rowIndex:
                return 0
            return arr[col]

        for i in range(1, rowIndex + 1):
            newArr = [0] * (rowIndex + 1)
            for j in range(i + 1):
                newArr[j] = getVal(i - 1, j - 1) + getVal(i - 1, j)
            arr = newArr
        return arr


if __name__ == '__main__':
    rowIndex = 4
    res = Solution().getRow(rowIndex)
    print(res)
