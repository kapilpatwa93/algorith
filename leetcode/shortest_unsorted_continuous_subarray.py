import math
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        unsortedStarted = False
        unsortedStart = 0
        lastUnsorted = 0
        unsortedEnd = 0
        unMax = -math.inf
        unMin = math.inf
        for i in range(0, len(nums)):
            if i < len(nums) - 1 and nums[i] - nums[i + 1] > 0:
                if not unsortedStarted:
                    unsortedStarted = True
                    unsortedStart = i
                lastUnsorted = i
                unMax = max(unMax, nums[i])
            if unsortedStarted:
                unMin = min(unMin, nums[i])

        for i in range(0, unsortedStart):
            if nums[i] > unMin:
                unsortedStart = i
                break

        for i in range(lastUnsorted + 1, len(nums)):
            if nums[i] >= unMax and unsortedStarted:
                unsortedEnd = i
                break
        if unsortedStarted and unsortedEnd == 0:
            unsortedEnd = len(nums)
        return unsortedEnd - unsortedStart

if __name__ == '__main__':
    nums = [1, 4, 5, 2, 3]
    res = Solution().findUnsortedSubarray(nums)
    print(res)