from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            # while start != end -1:

            mid = start + int((end - start) / 2)
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                start = mid + 1
            else:
                end = mid - 1

        if target < matrix[mid][0]:
            mid = mid - 1

        start = 0
        end = len(matrix[mid]) - 1
        row = matrix[mid]
        while start <= end:
            mid = start + int((end - start / 2))
            if row[mid] == target:
                return True
            elif target > row[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 25, 27, 28], [32, 34, 36, 37]]
    target = 36
    res = Solution().searchMatrix(matrix, target)
    print(res)
