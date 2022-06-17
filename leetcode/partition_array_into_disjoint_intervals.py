import math
from typing import List


class Solution:
    def partitionDisjoint1(self, nums: List[int]) -> int:
        maxPrefix = [0 for _ in nums]
        minSuffix = maxPrefix.copy()
        m = 0
        m1 = 10000000
        length = len(nums) - 1
        for i in range(len(nums)):
            m = max(nums[i], m)
            m1 = min(m1, nums[length - i])
            maxPrefix[i] = m
            minSuffix[length - i] = m1
        for i in range(length):
            if maxPrefix[i] <= minSuffix[i + 1]:
                return i + 1

    def partitionDisjoint(self, A: List[int]) -> int:
        maxi = A[0]

        allMax = A[0]

        solution = 1
        for i in range(1, len(A)):
            if A[i] < maxi:
                solution = i + 1
                maxi = allMax
            else:
                allMax = max(allMax, A[i])

        return solution


if __name__ == '__main__':
    nums = [ 4, 5, 6, 8, 6, 7, 4, 2, 4, 6, 7, 8, 9, 9]
    res = Solution().partitionDisjoint(nums)
    print(res)
