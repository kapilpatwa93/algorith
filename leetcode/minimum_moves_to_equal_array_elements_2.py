from math import floor, ceil
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        midIndex1 = floor(len(nums) / 2)
        midIndex2 = ceil(len(nums) / 2)
        total1 = 0
        total2 = 0
        for i in range(len(nums)):
            num = nums[i]
            total1 += abs(nums[midIndex1] - num)
            total2 += abs(nums[midIndex2] - num)
        return total1 if total1 < total2 else total2


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 2, 3, 5, 6, 9, 94, 3, 5, 3, 56, 3, 5, 6, 7, 8, 9, 9, 9, 9, 10]
    res = Solution().minMoves2(nums)
    print(res)
