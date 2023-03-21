from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        consecutiveCount = 0
        totalCount = 0
        for i in nums:
            if i != 0:
                totalCount += (consecutiveCount * (consecutiveCount + 1)) / 2
                consecutiveCount = 0
            else:
                consecutiveCount += 1
        totalCount += (consecutiveCount * (consecutiveCount + 1)) / 2
        return int(totalCount)


if __name__ == '__main__':
    nums = [1, 2, 0, 0, 1, 0, 0, 1, 0, 1]
    res = Solution().zeroFilledSubarray(nums)
    print(res)
